import os
import flask
import flask_login

from base_site import db
from base_site import bcrypt
from base_site.models import User
from base_site.models import Post
from base_site.users.utils import save_picture
from base_site.users.utils import send_reset_email
from base_site.users.forms import RegistrationForm
from base_site.users.forms import LoginForm
from base_site.users.forms import UpdateAccountForm
from base_site.users.forms import RequestResetForm, ResetPasswordForm

from flask import current_app as app

users = flask.Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                                form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flask.flash('Your account has been created!" \
            " You are now able to log in', 'success')
        return flask.redirect(flask.url_for('users.login'))
    return flask.render_template("users/register.html",
                                 title='Register',
                                 form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            flask_login.login_user(user, remember=form.remember.data)
            next_page = flask.request.args.get('next')
            if next_page:
                return flask.redirect(next_page)
            flask.redirect(flask.url_for('main.home'))
        else:
            flask.flash('Login unsuccessful," \
                " Please check your email and password!', 'danger')

    return flask.render_template("users/login.html",
                                 title='Login',
                                 form=form)


@users.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@flask_login.login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            flask_login.current_user.image_file = picture_file
        flask_login.current_user.username = form.username.data
        flask_login.current_user.email = form.email.data
        db.session.commit()

        flask.flash('Your account has been updated!', 'success')
        return flask.redirect(flask.url_for('users.account'))
    elif flask.request.method == 'GET':
        form.username.data = flask_login.current_user.username
        form.email.data = flask_login.current_user.email
    image_file = flask.url_for(
                    'static',
                    filename=os.path.join(
                        'profile_pics',
                        flask_login.current_user.image_file))
    return flask.render_template('users/account.html',
                                 title='Account',
                                 image_file=image_file,
                                 form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = flask.request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return flask.render_template("posts/user_posts.html",
                                 title='user_posts',
                                 posts=posts,
                                 user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        sender = app.config.get("MAIL_USERNAME")
        send_reset_email(user, sender)
        flask.flash('An email has been sent with instructions "\
            "to reset your password', 'info')
        return flask.redirect(flask.url_for('users.login'))
    return flask.render_template('users/reset_request.html',
                                 title='Reset Password',
                                 form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return flask.redirect(flask.url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                                form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flask.flash('Your password has been updated!" \
            " You are now able to log in', 'success')
        return flask.redirect(flask.url_for('users.login'))

    return flask.render_template('users/reset_token.html',
                                 title='Reset Password',
                                 form=form)


@users.route("/unsubcribe")
@flask_login.login_required
def unsubscribe():
    if flask_login.current_user.is_authenticated:
        # delete all the post
        posts = Post.query.filter_by(author=flask_login.current_user).all()
        for p in posts:
            db.session.delete(p)
        db.session.delete(flask_login.current_user)
        db.session.commit()
        flask_login.logout_user()
    return flask.redirect(flask.url_for('main.home'))


@users.route("/dump")
def dump():
    auth_state_key = app.config.get('AUTH_STATE_KEY')
    if 'auth_state_key' in flask.session:
        app.logger.info("AUTH", flask.session[auth_state_key])
    else:
        app.logger.info("no Key")
    return flask.redirect(flask.url_for('main.home'))
