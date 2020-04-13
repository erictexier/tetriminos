import flask
from flask_admin import BaseView, expose
from flask_login import current_user
from flask import current_app as app

class AdminDriveView(BaseView):
    @expose('/')
    def index(self):
        do_access = False
        domain = app.config.get("DOMAIN", "")
        if (current_user.is_authenticated and 
            domain in current_user.email):
            do_access = True
        options = {'title': domain.capitalize(),
                   'do_access': do_access}
        return self.render('admin/drive_admin.html', **options)
