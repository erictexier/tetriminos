import flask
from flask_admin import AdminIndexView
from flask_login import current_user


class AdminAppIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # app.logger.info("inaccessible_callback: {} / {}".format(name, kwargs))
        return flask.redirect(flask.url_for('main.home'))