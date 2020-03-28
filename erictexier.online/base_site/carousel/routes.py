# -*- coding: utf-8 -*-
import os
import pathlib
import flask
from flask import current_app as app
import base_site

carousel = flask.Blueprint('carousel', __name__)

static_path = pathlib.Path(
                        os.path.join(os.path.dirname(base_site.__file__),
                        'static'))


@carousel.route('/carousel')
def carousel_route():
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

    return flask.render_template("carousel/photo_slide.html",
                                 title='Photo Slide',
                                 image=image,
                                 others=others)
