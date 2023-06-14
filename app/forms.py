from flask_wtf import FlaskForm
from wtforms import SubmitField

class SubmitButton(FlaskForm):
    submit = SubmitField('Upload playlist')