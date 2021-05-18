from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import users

class RegistrationForm(FlaskForm):
    
      email = StringField('Email', validators=[DataRequired(), Email()])