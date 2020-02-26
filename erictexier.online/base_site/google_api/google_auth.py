# https://www.mattbutton.com/2019/01/05/google-authentication-with-python-and-flask/
import functools
import os

import flask

from authlib.integrations.requests_client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery


def is_logged_in():
    return True if AUTH_TOKEN_KEY in flask.session else False

def build_credentials():
    if not is_logged_in():
        raise Exception('User must be logged in')

    oauth2_tokens = flask.session[AUTH_TOKEN_KEY]

    return google.oauth2.credentials.Credentials(
                oauth2_tokens['access_token'],
                refresh_token=oauth2_tokens['refresh_token'],
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                token_uri=ACCESS_TOKEN_URI)

def get_user_info():

    credentials = build_credentials()
    oauth2_client = googleapiclient.discovery.build('oauth2', 'v2',
                                                    credentials=credentials)
    return oauth2_client.userinfo().get().execute()

