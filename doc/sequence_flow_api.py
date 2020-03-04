https://developers.google.com/identity/protocols/OAuth2WebServer

import google.oauth2.credentials
import google_auth_oauthlib.flow
import flask
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file("credentials.json", ['https://www.googleapis.com/auth/drive.metadata.readonly'])
flow.redirect_uri = 'https://erictexier.online/with_google/loging/callback'
authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')

authorization_response = flask.request.url
flow.fetch_token(authorization_response=authorization_response)

credentials = flow.credentials

flask.redirect(authorization_url)
# Store the credentials in the session.
# ACTION ITEM for developers:
#     Store user's access and refresh tokens in your data store if
#     incorporating this code into your real app.
credentials = flow.credentials

# live or put into database
flask.session['credentials'] = {
    'token': credentials.token,
    'refresh_token': credentials.refresh_token,
    'token_uri': credentials.token_uri,
    'client_id': credentials.client_id,
    'client_secret': credentials.client_secret,
    'scopes': credentials.scopes}