# -*- coding: utf-8 -*-

import flask

carousel = flask.Blueprint('carousel', __name__)


@carousel.route('/carousel')
def carousel_route():
    return flask.render_template("carousel/photo_slide.html",
                                 title='Photo Slide')
