# -*- coding: utf-8 -*-

import flask_wtf
import wtforms
from wtforms.validators import DataRequired


class TblForm(flask_wtf.FlaskForm):
    blogname = wtforms.StringField('Blog Name',
                                validators=[DataRequired()],default='letexman')
'''
    content = wtforms.StringField('Range',
                                validators=[DataRequired()])
    action = wtforms.StringField('Action',
                                validators=[DataRequired()])
    submit = wtforms.SubmitField('Reload')
'''