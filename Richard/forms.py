from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Email

from .data_processing import getDefault


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4,max=80)])
    retypePassword = PasswordField('Retype Password', validators=[InputRequired(), Length(min=4,max=80)])
    #email = StringField('Email (optional)', validators=[Email(message = 'Invalid Email'), Length(max=50)])
    #phone = IntegerField('Phone Number', validators=[])
    submit = SubmitField('Add User')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4,max=80)])
    submit = SubmitField('Log In to Dashboard')

class AuthGitUserForm(FlaskForm):
    username = StringField('Github Username', validators = [InputRequired()])
    submit = SubmitField('Authenticate User')



class UserSettingsForm(FlaskForm):
    default = ['Dark']
    colourThemeChoices = ['Dark', 'Light'] #could be value,label pairs
    colourTheme = SelectField('Colour Theme', choices=colourThemeChoices, default=default[0])
    submit = SubmitField('UPDATE')

