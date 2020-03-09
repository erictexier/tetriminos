# -*- coding: utf-8 -*-

# https://mattbutton.com/2019/01/05/google-authentication-with-python-and-flask/

import os
import functools
import flask
import requests

from authlib.integrations.requests_client import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient
import google.oauth2.credentials
import googleapiclient.discovery


def is_logged_in():
    k = os.environ.get('AUTH_TOKEN_KEY', "")
    if k and k in flask.session:
        return True
    return False


def build_credentials(option):
    if not is_logged_in():
        raise Exception('User must be logged in')

    CLIENT_ID = option.get("CLIENT_ID", None)
    CLIENT_SECRET = option.get("CLIENT_SECRET", None)
    AUTH_TOKEN_KEY = option.get("AUTH_TOKEN_KEY", None)
    ACCESS_TOKEN_URI = option.get("ACCESS_TOKEN_URI")
    oauth2_tokens = flask.session[AUTH_TOKEN_KEY]

    return google.oauth2.credentials.Credentials(
                oauth2_tokens['access_token'],
                refresh_token=oauth2_tokens['refresh_token'],
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                token_uri=ACCESS_TOKEN_URI)


def get_user_info():

    credentials = build_credentials()
    oauth2_client = googleapiclient.discovery.build('oauth2',
                                                    'v2',
                                                    credentials=credentials)
    return oauth2_client.userinfo().get().execute()


def get_client(client_id):
    """ should maybe become a singleton  with """
    if client_id in ['', None]:
        return None
    return WebApplicationClient(client_id)


def get_google_provider_cfg(a_discovery_url):
    return requests.get(a_discovery_url).json()
