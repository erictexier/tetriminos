import flask_wtf
import wtforms
from wtforms.validators import DataRequired

class PostForm(flask_wtf.FlaskForm):
    title = wtforms.StringField('Title', validators = [DataRequired()])
    content = wtforms.TextAreaField('Content', validators = [DataRequired()])
    submit = wtforms.SubmitField('Post')
