import os
import flask
from flask import current_app as app
from werkzeug.utils import secure_filename

resume = flask.Blueprint('resume', __name__)

@resume.route("/cv")
def resume_route():
    folder = app.config.get("MEDIA_FOLDER", "")
    print("folder %s" % folder)
    afile = os.path.join(folder,'RESUME.pdf')
    return flask.send_file(afile)