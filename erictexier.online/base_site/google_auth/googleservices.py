# -*- coding: utf-8 -*-

import os
import functools
import flask
import requests
import json

import google.oauth2.credentials
import googleapiclient.discovery
import google_auth_oauthlib.flow


class GoogleServices(object):
    API_SERVICE_NAME_DRIVE = 'drive'
    API_VERSION_DRIVE = 'v3'
    API_SERVICE_NAME_GMAIL = 'gmail'
    API_VERSION_GMAIL = 'v1'

    API_REVOKE_HTTP = 'https://oauth2.googleapis.com/revoke'

    @staticmethod
    def get_token_in(configdata):
        k = configdata.get('AUTH_TOKEN_KEY', "")
        if k and k in configdata:
            return configdata.get(k)
        return None

    @staticmethod
    def is_token_exist(configdata):
        k = configdata.get('AUTH_TOKEN_KEY', "")
        if k and k in configdata:
            path = configdata.get(k)
            if os.path.exists(path):
                return True
        return False

    @staticmethod
    def unset_token(configdata):
        k = configdata.get('AUTH_TOKEN_KEY', "")
        if k and k in configdata:
            configdata.update({k: ""})

    @staticmethod
    def get_credentials(**token):
        return google.oauth2.credentials.Credentials(**token)

    @staticmethod
    def get_drive_service(credentials):
        return googleapiclient.discovery.build(
                                        GoogleServices.API_SERVICE_NAME_DRIVE,
                                        GoogleServices.API_VERSION_DRIVE,
                                        cache_discovery=False,
                                        credentials=credentials)

    @staticmethod
    def get_gmail_service(credentials):
        return googleapiclient.discovery.build(
                                        GoogleServices.API_SERVICE_NAME_GMAIL,
                                        GoogleServices.API_VERSION_GMAIL,
                                        cache_discovery=False,
                                        credentials=credentials)

    @staticmethod
    def init_flow_authorize(configdata, state=None):
        # Create flow instance to manage the OAuth 2.0 Authorization
        # Grant Flow steps.
        client_sfile = configdata.get("CLIENT_SECRETS_FILE", "")
        if os.path.exists(client_sfile) is False:
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
                                                state=state)

    @staticmethod
    def credentials_to_file(configdata, credentials):
        """ we bind the secret file to a token file """
        dict_credential = {
                            'token': credentials.token,
                            'refresh_token': credentials.refresh_token,
                            'token_uri': credentials.token_uri,
                            'client_id': credentials.client_id,
                            'client_secret': credentials.client_secret,
                            'scopes': credentials.scopes
                        }
        client_sfile = configdata.get("CLIENT_SECRETS_FILE", "")
        k = configdata.get('AUTH_TOKEN_KEY', "")
        if client_sfile != "":
            out_file = os.path.splitext(client_sfile)[0] + ".token"
            with open(out_file, 'w') as file:
                file.write(json.dumps(dict_credential))
        if k:
            if os.path.exists(out_file):
                configdata.update({k: out_file})
            else:
                configdata.update({k: ""})

    @staticmethod
    def load_token(configdata):
        out_file = GoogleServices.get_token_in(configdata)
        if out_file and os.path.exists(out_file):
            with open(out_file, 'r') as file:
                dict_credential = json.load(file)
                return dict_credential
        return None
