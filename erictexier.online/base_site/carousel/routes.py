# -*- coding: utf-8 -*-
import os
import pathlib
import flask
from flask import current_app as app
import base_site

from base_site.services import pytumblr

url = '/v2/blog/letexman/posts'
limit_request = {'limit':103, 'offset':200}

carousel = flask.Blueprint('carousel', __name__)

static_path = pathlib.Path(
                        os.path.join(os.path.dirname(base_site.__file__),
                        'static'))
"""
r = client.send_api_request('get',url)

r = client.send_api_request('get',url,params=d,valid_parameters=['limit','offset'])
pp = r['posts']
x = pp[0]['photos'][0]['original_size']['url']
r['blog']['posts']
"""
@carousel.route('/carousel')
def carousel_route():


    client = pytumblr.TumblrRestClient.get_tumblr_client(
                                    app.config['TBL_TOKEN_CREDENTIAL'])

    rep = client.send_api_request(
                                'get',
                                url,
                                params=limit_request,
                                valid_parameters=['limit','offset'])

    tumblr_posts = rep['posts']
    others = []
    for p in tumblr_posts:
            src= p['photos'][0]['original_size']['url']
            print(src)
            others.append(src)
    """
    _sub_dir = "slides"
    # basic use of static... not good
    try:
        all_ima = os.listdir(static_path.joinpath(_sub_dir))
    except:
        return "no images available, sorry"

    image = os.path.join('slides', all_ima[0])
    others = []
    for im in all_ima[1:]:
        others.append(os.path.join(_sub_dir, im))
    """
    return flask.render_template("carousel/photo_slide.html",
                                 title='Photo Slide',
                                 image=others[0],
                                 others=others[1:])
