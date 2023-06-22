from flask_wtf import FlaskForm
from wtforms import SubmitField

class SubmitButton(FlaskForm):
    submit = SubmitField('Upload Spotify playlist')

class RefreshButton(FlaskForm):
    submit = SubmitField('Generate another name')

class PickPlaylistButton(FlaskForm):
    submit = SubmitField('Choose a different playlist')

class HomeButton(FlaskForm):
    submit = SubmitField('Home')