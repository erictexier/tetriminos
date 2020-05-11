# -*- coding: utf-8 -*-
import os
import random

import flask
from flask import current_app as app
from base_site.services import pytumblr
from base_site.carousel.tbl_display import TblDisplay


url = '/v2/blog/letexman/posts'
limit_request = {'limit':300, 'offset':1050}

carousel = flask.Blueprint('carousel', __name__)

@carousel.route("/")
@carousel.route('/carousel')
def carousel_route():


    client = pytumblr.TumblrRestClient.get_tumblr_client(
                                    app.config['TBL_TOKEN_CREDENTIAL'])

    if client:
        rep = client.send_api_request(
                                    'get',
                                    url,
                                    params=limit_request,
                                    valid_parameters=['limit','offset'])

        tumblr_posts = rep['posts']
        post_list = list()

        for p in tumblr_posts:
            newp = TblDisplay(p)
            if newp.is_valid():
                post_list.append(newp)
        print("nb if photo",len(post_list))
        random.shuffle(post_list)
    return flask.render_template("carousel/photo_slide.html",
                                 title='Photo Slide',
                                 image=post_list[0],
                                 others=post_list[1:])
