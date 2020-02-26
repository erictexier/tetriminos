from flask import Blueprint
from flask import render_template, jsonify, flash, request, redirect, url_for, current_app
from base_site.google_api import google_auth
from authlib.integrations.requests_client import OAuth2Session

google_api = Blueprint('google_api', __name__)

@google_api.route('/with_google')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    return 'You are not currently logged in.'

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
    CLIEND_ID = app.config.get("CLIENT_ID", None)
    CLIEND_SECRET = app.config.get("CLIENT_SECRET", None)
    if CLIEND_ID and CLIEND_SECRET:
        session = OAuth2Session(CLIENT_ID,
                                CLIENT_SECRET,
                                scope = app.config.get("AUTHORIZATION_SCOPE","openid"),
                                redirect_uri = app.config.get("AUTH_REDIRECT_URI")
    
        uri, state = session.authorization_url(AUTHORIZATION_URL)

        flask.session[AUTH_STATE_KEY] = state
        flask.session.permanent = True

        return flask.redirect(uri, code=302)
    return 'You are not currently able to log in.'

@google_api.route('/with_google/auth')
@no_cache
def google_auth_redirect():
    req_state = flask.request.args.get('state', default=None, type=None)

    if req_state != flask.session[AUTH_STATE_KEY]:
        response = flask.make_response('Invalid state parameter', 401)
        return response

    session = OAuth2Session(CLIENT_ID, CLIENT_SECRET,
                            scope=AUTHORIZATION_SCOPE,
                            state=flask.session[AUTH_STATE_KEY],
                            redirect_uri=AUTH_REDIRECT_URI)

    oauth2_tokens = session.fetch_access_token(
                        ACCESS_TOKEN_URI,
                        authorization_response=flask.request.url)

    flask.session[AUTH_TOKEN_KEY] = oauth2_tokens
    return flask.redirect(BASE_URI, code=302)

@google_api.route('/with_google/logout')
@no_cache
def logout():
    flask.session.pop(AUTH_TOKEN_KEY, None)
    flask.session.pop(AUTH_STATE_KEY, None)

    return flask.redirect(BASE_URI, code=302)