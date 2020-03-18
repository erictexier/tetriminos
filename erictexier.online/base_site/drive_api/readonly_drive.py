# -*- coding: utf-8 -*-
# https://developers.google.com/identity/protocols/OAuth2WebServer
import os
import flask
from flask import Blueprint
from flask import current_app as app
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

#from base_site.google_api import google_auth
from base_site.google_api import mail_utils

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
API_SERVICE_NAME = 'drive'
API_VERSION = 'v3'

drive_api = Blueprint('drive_api', __name__)


from base_site.google import google_auth


@drive_api.route('/drive_api')
def route_drive_index():
    return print_index_table()


@drive_api.route('/drive_api/test_api_request')
def test_api_request():
    print("TRY"*20)
    if 'credentials' not in flask.session:
        return flask.redirect(flask.url_for('drive_api.authorize'))

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
                                        **flask.session['credentials'])

    drive = googleapiclient.discovery.build(API_SERVICE_NAME,
                                            API_VERSION,
                                            cache_discovery=False,
                                            credentials=credentials)


    data = mail_utils.create_message("erictexier@eclecticstudionet.com",
                                     "e.texier@icloud.com",
                                     "bonjour de bonjour", "Rien a dire")

    mails = googleapiclient.discovery.build('gmail',
                                            'v1',
                                            cache_discovery=False,
                                            credentials=credentials)

    user_id = credentials.client_id
    print(mails.users())
    msg = mail_utils.send_message(mails, "me", data)
    results = mails.users().labels().list(userId='me').execute()
    print(results)
    files = drive.files().list().execute()

    # Save credentials back to session in case access token was refreshed.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    flask.session['credentials'] = credentials_to_dict(credentials)

    #return flask.jsonify(**files)
    return flask.jsonify(**results)


@drive_api.route('/drive_api/authorize')
def authorize():
    # Create flow instance 
    flow = google_auth.init_flow_authorize(app.config)

    print("IN AUTHORIZE"*10)
    # The URI created here must exactly match one of the authorized redirect
    # URIs for the OAuth 2.0 client, which you configured in the API Console.
    # If this value doesn't match an authorized URI, you will get a
    # 'redirect_uri_mismatch' error.
    flow.redirect_uri = flask.url_for('drive_api.oauth2callback',
                                      _external=True)

    authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token
            # without re-prompting the user for permission. Recommended for web
            # server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')

    print("authorization_url" * 199,authorization_url)

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@drive_api.route('/drive_api/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    
    flow = google_auth.init_flow_authorize(app.config,
                                           state = flask.session['state'])
    flow.redirect_uri = flask.url_for('drive_api.oauth2callback',
                                      _external=True)
    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    print("y"*100) 
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)

    print(flask.session['credentials'])
    print("z"*100) 
    return flask.redirect(flask.url_for('drive_api.test_api_request'))


@drive_api.route('/drive_api/revoke')
def revoke():
    if 'credentials' not in flask.session:
        return('You need to <a href="/drive_api/authorize">authorize</a>' +
                'before testing the code to revoke credentials.')

    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    revoke = requests.post(
                'https://oauth2.googleapis.com/revoke',
                params={'token': credentials.token},
                headers={'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return('Credentials successfully revoked.' + print_index_table())
    else:
        return('An error occurred.' + print_index_table())


@drive_api.route('/drive_api/clear')
def clear_credentials():
    if 'credentials' in flask.session:
        del flask.session['credentials']
    return ('Credentials have been cleared.<br><br>' +
            print_index_table())


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}


def print_index_table():
    return (
        '<table>' +
        '<tr><td><a href="/drive_api/test_api_request">Test an API request</a></td>' +
        '<td>Submit an API request and see a formatted JSON response. ' +
        '    Go through the authorization flow if there are no stored ' +
        '    credentials for the user.</td></tr>' +
        '<tr><td><a href="/drive_api/authorize">Test the auth flow directly</a></td>' +
        '<td>Go directly to the authorization flow. If there are stored ' +
        '    credentials, you still might not be prompted to reauthorize ' +
        '    the application.</td></tr>' +
        '<tr><td><a href="/drive_api/revoke">Revoke current credentials</a></td>' +
        '<td>Revoke the access token associated with the current user ' +
        '    session. After revoking credentials, if you go to the test ' +
        '    page, you should see an <code>invalid_grant</code> error.' +
        '</td></tr>' +
        '<tr><td><a href="/drive_api/clear">Clear Flask session credentials</a></td>' +
        '<td>Clear the access token currently stored in the user session. ' +
        '    After clearing the token, if you <a href="/drive_api/test_api_request">test the ' +
        '    API request</a> again, you should go back to the auth flow.' +
        '</td></tr></table>')
