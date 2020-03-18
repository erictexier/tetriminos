# -*- coding: utf-8 -*-

import os
import flask
from flask import Blueprint
from flask import current_app as app
import requests

from base_site.google_auth.googleservices import GoogleServices
from base_site.google_auth import mail_utils

google_service = Blueprint('google_service', __name__)


@google_service.route('/google_service')
def route_drive_index():
    return print_index_table()


@google_service.route('/google_service/test_api_request')
def test_api_request():

    creds = GoogleServices.load_token(app.config)
    if creds is None:
        return flask.redirect(flask.url_for('google_service.authorize'))
    credentials = GoogleServices.get_credentials(**creds)
    # drive example
    drive = GoogleServices.get_drive_service(credentials)
    files = drive.files().list().execute()

    # email example
    mails = GoogleServices.get_gmail_service(credentials)
    data = mail_utils.create_message(
                        app.config.get("MAIL_USERNAME"),
                        "e.texier@icloud.com",
                        "bonjour de bonjour", "Rien a dire")

    msg = mail_utils.send_message(mails, "me", data)
    results = mails.users().labels().list(userId="me").execute()
    GoogleServices.credentials_to_file(app.config, credentials)

    return flask.jsonify(**results)


@google_service.route('/google_service/authorize')
def authorize():
    # Create flow instance 
    flow = GoogleServices.init_flow_authorize(app.config)
    # The URI created here must exactly match one of the authorized redirect
    # URIs for the OAuth 2.0 client, which you configured in the API Console.
    # If this value doesn't match an authorized URI, you will get a
    # 'redirect_uri_mismatch' error.
    flow.redirect_uri = flask.url_for('google_service.oauth2callback',
                                      _external=True)

    authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token
            # without re-prompting the user for permission. Recommended for web
            # server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@google_service.route('/google_service/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    
    flow = GoogleServices.init_flow_authorize(
                                           app.config,
                                           state = flask.session['state'])
    flow.redirect_uri = flask.url_for('google_service.oauth2callback',
                                      _external=True)
    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)
    GoogleServices.credentials_to_file(app.config, flow.credentials)

    return flask.redirect(flask.url_for('google_service.test_api_request'))


@google_service.route('/google_service/revoke')
def revoke():

    if GoogleServices.is_token_exist(app.config) is False:
        return('You need to <a href="/google_service/authorize">authorize</a>' +
                'before testing the code to revoke credentials.')

    token = GoogleServices.load_token(app.config)
    credentials = GoogleServices.get_credentials(**token)

    revoke = requests.post(
                GoogleServices.API_REVOKE_HTTP,
                params={'token': credentials.token},
                headers={'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return('Credentials successfully revoked.' + print_index_table())
    else:
        return('An error occurred.' + print_index_table())


@google_service.route('/google_service/clear')
def clear_credentials():
    GoogleServices.unset_token(app.config)
    return ('Credentials have been cleared.<br><br>' +
            print_index_table())

def print_index_table():
    return (
        '<table>' +
        '<tr><td><a href="/google_service/test_api_request">Test an API request</a></td>' +
        '<td>Submit an API request and see a formatted JSON response. ' +
        '    Go through the authorization flow if there are no stored ' +
        '    credentials for the user.</td></tr>' +
        '<tr><td><a href="/google_service/authorize">Test the auth flow directly</a></td>' +
        '<td>Go directly to the authorization flow. If there are stored ' +
        '    credentials, you still might not be prompted to reauthorize ' +
        '    the application.</td></tr>' +
        '<tr><td><a href="/google_service/revoke">Revoke current credentials</a></td>' +
        '<td>Revoke the access token associated with the current user ' +
        '    session. After revoking credentials, if you go to the test ' +
        '    page, you should see an <code>invalid_grant</code> error.' +
        '</td></tr>' +
        '<tr><td><a href="/google_service/clear">Clear Flask session credentials</a></td>' +
        '<td>Clear the access token currently stored in the user session. ' +
        '    After clearing the token, if you <a href="/google_service/test_api_request">test the ' +
        '    API request</a> again, you should go back to the auth flow.' +
        '</td></tr></table>')
