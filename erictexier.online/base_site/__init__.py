# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from base_site.config import Config

import logging
from logging.config import dictConfig

logdict = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}

logging.config.dictConfig(logdict)
logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from base_site.users.routes import users
    from base_site.posts.routes import posts
    from base_site.main.routes import main
    from base_site.fillit.routes import fillit
    from base_site.carousel.routes import carousel
    from base_site.errors.handlers import errors
    from base_site.google_auth.routes import google_service

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(fillit)
    app.register_blueprint(carousel)
    app.register_blueprint(google_service)
    app.register_blueprint(errors)
    app.logger.info("%s created" % __name__)
    return app
