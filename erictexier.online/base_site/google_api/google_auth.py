# -*- coding: utf-8 -*-

# https://mattbutton.com/2019/01/05/google-authentication-with-python-and-flask/

import os
import functools
import flask
import requests
import json
import base64
#import logging
#logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

from authlib.integrations.requests_client import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient
import google.oauth2.credentials
import googleapiclient.discovery
import google_auth_oauthlib.flow

def is_token_in():
    k = os.environ.get('AUTH_TOKEN_KEY', "")
    if k and k in flask.session:
        return True
    return False

def init_flow_authorize(configdata, state=None):
    # Create flow instance to manage the OAuth 2.0 Authorization
    # Grant Flow steps.
    client_sfile = configdata.get("CLIENT_SECRETS_FILE", "")
    if client_sfile != "" and os.path.exists(client_sfile) is False:
        return None
    scopes = configdata.get("AUTHORIZATION_SCOPE", "")

    if scopes == "":
        return None

    if state:
        return google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                                            client_sfile, scopes=scopes)
    return google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                                            client_sfile,
                                            scopes=scopes,
                                            state = state)


def credentials_to_file(credentials, configdata):
    """ we bind the secret file to a token file """
    dict_credential =  {'token': credentials.token,
                        'refresh_token': credentials.refresh_token,
                        'token_uri': credentials.token_uri,
                        'client_id': credentials.client_id,
                        'client_secret': credentials.client_secret,
                        'scopes': credentials.scopes}
    client_sfile = configdata.get("CLIENT_SECRETS_FILE", "")
    k = configdata.get('AUTH_TOKEN_KEY', "")
    if client_secret_file != "" and k != "":
        out_file = os.path.splitext(client_sfile)[0] + ".token"
        configdata.set(k, base64.encodestring(bytes(out_file,'utf-8')))
        with open(out_file, 'w') as file:
            file.write(json.dumps(dict_credential))
    else:
        configdata.set(k, base64.encodestring(bytes('','utf-8')))


def load_token():
    k = configdata.get('AUTH_TOKEN_KEY', "")
    if k != "":
        out_file = configdata.get(k)
        with open(out_file, 'r') as file:
            dict_credential = json.load(file))
        return dict_credential
    return dict()

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
