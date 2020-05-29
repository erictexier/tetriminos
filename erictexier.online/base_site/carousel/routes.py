# -*- coding: utf-8 -*-
import os
import random
from pprint import pprint

import random
import flask
from flask import current_app as app
from base_site.services import pytumblr
from base_site.carousel.tbl_display import TblDisplay
from base_site.carousel.forms import TblForm

carousel = flask.Blueprint('carousel', __name__)

CURRENT_BLOG = 'letexman'

POST_LIST = [
            {'blog': {'description': '',
          'name': 'riversidestandpipe',
          'title': 'The standpipe of Riverside',
          'updated': 1353030831,
          'url': 'https://riversidestandpipe.tumblr.com/',
          'uuid': 't:Jhizo61jjHqvrcjNYAjAiQ'},
 'blog_name': 'riversidestandpipe',
 'caption': "I'm neat, what can I say?",
 'date': '2012-09-04',
 'image_permalink': '',
 'mult_url': [{'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo2_1280.jpg',
               'width': 1280},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo3_1280.jpg',
               'width': 1280},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo4_1280.jpg',
               'width': 1280},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo5_1280.jpg',
               'width': 1280},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo6_1280.jpg',
               'width': 1280},
              {'height': 1536,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo7_1280.jpg',
               'width': 1024},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo8_1280.jpg',
               'width': 1280},
              {'height': 853,
               'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo9_1280.jpg',
               'width': 1280}],
 'pic_url': {'height': 853,
             'url': 'https://66.media.tumblr.com/tumblr_m9swe1UtT01rfc6evo1_1280.jpg',
             'width': 1280},
 'tags': ['water', 'standpipe']}

        ]

def get_client():
    return pytumblr.TumblrRestClient.get_tumblr_client(
                                app.config['TBL_TOKEN_CREDENTIAL'])


def reset_carousel(client, offset, blog_name):
    offset_rand = random.randint(10, offset)
    limit_request = {'limit': 5, 'offset':offset_rand}
    url = '/v2/blog/%s/posts' % blog_name

    rep = client.send_api_request('get',
                                  url,
                                  params=limit_request,
                                  valid_parameters=['limit','offset'])

    tumblr_posts = rep['posts']
    post_list = list()
    for p in tumblr_posts:
        newp = TblDisplay()
        newp.from_data_tumblr(p)
        # print(newp)
        if newp.is_valid():
            post_list.append(newp)
    # print("nb of photo", len(post_list), limit_request)
    random.shuffle(post_list)
    if len(post_list) == 0:
        post_list = POST_LIST
    return post_list

def followers(client):
    rep = client.following(**{'offset': 0, 'limit': 50})
    return [x['name'] for x in rep['blogs']]

@carousel.route('/carousel', methods=['GET', 'POST'])
def carousel_route():
    form = TblForm()
    if form.validate_on_submit():
        print("carousel  POST",str(form.blogname.data))
        CURRENT_BLOG = str(form.blogname.data)
        client = get_client()
        post_list = reset_carousel(client, 50, form.blogname.data)
        follow = followers(client)
        CURRENT_BLOG = form.blogname.data
        return flask.render_template(
                                    'carousel/jacket.html',
                                    title='Photo Slide',
                                    image=post_list[0],
                                    others=post_list[1:],
                                    following=follow,
                                    form=form)

    if flask.request.method == 'GET':
        if form.blogname.data.strip() == "":
            form.blogname.data = CURRENT_BLOG
        print("carousel  GET")
        client = get_client()
        post_list = reset_carousel(client, 1000, form.blogname.data)
        follow = followers(client)
        return flask.render_template("carousel/photo_slide.html",
                                    title='Photo Slide',
                                    image=post_list[0],
                                    others=post_list[1:],
                                    following=follow,
                                    form=form)
    return flask.redirect(flask.url_for('carousel.carousel_route'))

@carousel.route('/carousel_ajax', methods=['POST'])
def carousel_ajax():
    form = TblForm()
    if not form.validate_on_submit():
        return flask.jsonify({"success": False})
    client = get_client()
    post_list = reset_carousel(client, 50, form.blogname.data)
    follow = followers(client)
    print("carousel POST AJAX", form.blogname.data)
    CURRENT_BLOG = form.blogname.data
    html = flask.render_template(
                                'carousel/jacket.html',
                                title='Photo Slide',
                                image=post_list[0],
                                others=post_list[1:],
                                following=follow,
                                form=form)
    return flask.jsonify({'html': html,
                          'success': True})

