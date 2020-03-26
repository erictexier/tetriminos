import flask
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class AdminUserModelView(ModelView):
    column_exclude_list = ['password',]
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):

        return flask.redirect(flask.url_for('main.home'))