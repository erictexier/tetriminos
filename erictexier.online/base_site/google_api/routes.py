# -*- coding: utf-8 -*-

import os
import functools
import json
#from authlib.integrations.requests_client import OAuth2Session
from requests_oauthlib import OAuth2Session
import requests

import flask
from flask import Blueprint
from flask import current_app as app
from base_site.google_api import google_auth


google_api = Blueprint('google_api', __name__)

def no_cache(view):
    @functools.wraps(view)
    def no_cache_impl(*args, **kwargs):
        response = flask.make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return functools.update_wrapper(no_cache_impl, view)


@google_api.route('/with_google/login')
@no_cache
def login():
    client_id = app.config.get("CLIENT_ID", None)
    client_secret = app.config.get("CLIENT_SECRET", None)
    discovery_url = app.config.get("DISCOVERY_URL")
    scope = app.config.get("AUTHORIZATION_SCOPE","openid")
    if client_id and client_secret:
        client = google_auth.get_client(client_id)
        provider_cfg = google_auth.get_google_provider_cfg(discovery_url)
        authorization_endpoint = provider_cfg["authorization_endpoint"]

        # Use library to construct the request for Google login and provide
        # scopes that let you retrieve user's profile from Google
        request_uri = client.prepare_request_uri(
                                    authorization_endpoint,
                                    redirect_uri=flask.request.base_url + "/callback",
                                    scope=scope,)
        return flask.redirect(request_uri)

    return flask.redirect(flask.url_for('users.register'))


@google_api.route('/with_google/login/callback')
def loggin_call_back():
    code = flask.request.args.get("code")
    if code == None:
        return flask.redirect(flask.url_for('users.register'))
    provider_cfg = google_auth.get_google_provider_cfg(app.config.get("DISCOVERY_URL"))
    token_endpoint = provider_cfg["token_endpoint"]
    client_id = app.config.get("CLIENT_ID", None)
    client_secret = app.config.get("CLIENT_SECRET", None)
    client = google_auth.get_client(client_id)
    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(token_endpoint,
                                                            authorization_response=flask.request.url,
                                                            redirect_url=flask.request.base_url,
                                                            code=code)
    token_response = requests.post(
                                token_url,
                                headers=headers,
                                data=body,
                                auth=(client_id, client_secret),)
    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        app.logger.info(unique_id,users_email,picture,users_name,)
        return " IN PROGRESS FOR NOW "
    else:
        return "User email not available or not verified by Google.", 400