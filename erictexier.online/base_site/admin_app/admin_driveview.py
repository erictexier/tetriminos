import flask
from flask_admin import BaseView, expose
from flask_login import current_user


class AdminDriveView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/drive_admin.html')
