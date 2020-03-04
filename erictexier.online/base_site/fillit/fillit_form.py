# -*- coding: utf-8 -*-

import flask_wtf
import wtforms
from wtforms.validators import DataRequired, NumberRange, Optional, InputRequired

class FillitForm(flask_wtf.FlaskForm):
    nb_element = wtforms.IntegerField('Tetriminos (max 13)', validators=[DataRequired(), 
												NumberRange(
													min=1,
													max=13, 
													message="nb of tetriminos should be between 1 and 26")])
    doletter = wtforms.SelectField('',  choices=[('Do 3D','3D'),
                                                    ('Do Color', 'Rect'),
                                                    ('Do Text', 'Text'),
                                                    ('Do Anim','Anim'),
                                                    ])
    submit = wtforms.SubmitField('Go')
