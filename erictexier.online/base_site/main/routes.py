# -*- coding: utf-8 -*-
import flask
from base_site.models import Post

main = flask.Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page = flask.request.args.get('page',1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5)
    return flask.render_template("posts/home.html", title = 'Posts', posts = posts)

@main.route("/about")
def about():
    alist = ["To be about what you decided on your personal drive:"]
    alist.append("Nothing for now :)")
    return flask.render_template("main/about.html", title = 'About Page In the work', contents= alist)
