import flask
from flask_admin import BaseView, expose
from flask_login import current_user

PROJECT_DEFAULT = "eclecticstudionet"

class AdminDriveView(BaseView):
    @expose('/')
    def index(self):
        do_access = False
        if PROJECT_DEFAULT in current_user.email:
            do_access = True
        options = {'title': PROJECT_DEFAULT,
                   'do_access': do_access}
        return self.render('admin/drive_admin.html', **options)
