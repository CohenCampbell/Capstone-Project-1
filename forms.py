from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, HiddenField, IntegerField
from wtforms.validators import Length, InputRequired

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=20, min=1)])

    password = PasswordField("Password", validators=[InputRequired(), Length(min=1)])
                             
    email = EmailField("Email", validators=[InputRequired(), Length(min=1)])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(max=20, min=1)])

    password = PasswordField("Password", validators=[InputRequired(), Length(min=1)])

class SpotifyPodcastSearchForm(FlaskForm):
    search = StringField("Search", validators=[Length(min=1)])

class KeywordForm(FlaskForm):
    keyword = StringField("Keyword", validators=[Length(min=1)])
    offset = IntegerField("Episode Offset")

class SpotifyPodcastInfoForm(FlaskForm):
    host= HiddenField("host")
    title= HiddenField("title")
    description = HiddenField("description")
    img_url= HiddenField("img_url")
    podcast_id_spotify= HiddenField("podcast_id_spotify")