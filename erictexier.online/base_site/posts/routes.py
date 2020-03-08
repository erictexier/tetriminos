# -*- coding: utf-8 -*-

import flask
from flask_login import login_required
from flask_login import current_user
from base_site.posts.forms import PostForm
from base_site.models import Post
from base_site import db

posts = flask.Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flask.flash("Your post has been created!", 'success')
        return flask.redirect(flask.url_for('main.home'))
    return flask.render_template('posts/create_post.html',
                                 title='New Post',
                                 legend='New Post',
                                 form=form)


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return flask.render_template('posts/post.html',
                                 title=post.title,
                                 post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flask.abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flask.flash('Your post has been updated!', 'success')
        return flask.redirect(flask.url_for('posts.post', post_id=post.id))
    elif flask.request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return flask.render_template('posts/create_post.html',
                                 title='Update Post',
                                 legend='Update Post',
                                 form=form)


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flask.abort(403)
    db.session.delete(post)
    db.session.commit()
    flask.flash('Your post has been deleted!', 'success')
    return flask.redirect(flask.url_for('main.home'))
