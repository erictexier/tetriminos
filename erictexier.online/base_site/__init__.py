from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from base_site.config import Config

"""
import os
import logging
from pprint import pformat
logging.log(logging.WARNING,pformat(os.environ['PYTHONPATH']))
"""

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class = Config):
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
    from base_site.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(fillit)
    app.register_blueprint(errors)

    return app
