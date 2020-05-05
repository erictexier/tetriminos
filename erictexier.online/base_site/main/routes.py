# -*- coding: utf-8 -*-
import flask
from base_site.models import Post
from werkzeug.utils import secure_filename

main = flask.Blueprint('main', __name__)

@main.route("/home")
def home():
    page = flask.request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
                    Post.date_posted.desc()).paginate(page=page, per_page=5)
    return flask.render_template("posts/home.html", title='Posts', posts=posts)


@main.route("/about")
def about():
    alist = ["To be about what you decided on your personal drive:"]
    alist.append("Nothing for now :)")
    return flask.render_template("main/about.html",
                                 title='About Page In the work',
                                 contents=alist)

@main.route("/contact")
def contact():
    alist = ["To be about what you decided on your personal drive:"]
    alist.append("Nothing for now :)")
    return flask.render_template("main/about.html",
                                 title='About Page In the work',
                                 contents=alist)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return flask.redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return flask.redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return flask.redirect(
                                url_for('uploaded_file',
                                filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''