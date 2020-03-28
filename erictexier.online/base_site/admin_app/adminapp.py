import flask
from flask_admin import Admin

from base_site.admin_app.admin_index import AdminAppIndexView
from base_site.admin_app.admin_userview import AdminUserModelView
from base_site.admin_app.admin_driveview import AdminDriveView

class AdminApp(Admin):

    def init_app(self, app, **kwargs):
        from base_site.models import User
        from base_site import db
        kwargs.update({'index_view': AdminAppIndexView()})
        super(AdminApp, self).init_app(app, **kwargs)
        self.add_view(AdminDriveView(name='Drive', endpoint='drivet'))
        self.add_view(AdminUserModelView(User,
                                         db.session,
                                         category="Database"))