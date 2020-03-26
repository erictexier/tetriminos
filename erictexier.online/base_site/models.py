# -*- coding: utf-8 -*-

from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask import current_app
from flask_login import UserMixin
from base_site import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """ function require but the extension LoginManager """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),
                           nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',
                            backref='author',
                            primaryjoin="User.id == Post.user_id",
                            lazy='dynamic')
    # active = db.Column(db.Boolean)
    # confirmed_at = db.Column(db.DateTime)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


"""
roles_users = db.Table(
                'roles_user',
                db.Column('user_id', db.Integer, db.ForeignKey('user_id')),
                db.Column('role_id', db.Integer, db.ForeignKey('role_id')))

class Role(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))


class OAuth(db.Model, OAuthConsumerMixin):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
"""

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
