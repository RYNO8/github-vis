from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    url = SelectField("URL: ", choices=[("languages", "languages"), ("contributors", "contributors")])
    owner = StringField("Owner: ")
    repo = StringField("Repo: ")
    submit = SubmitField("OK")