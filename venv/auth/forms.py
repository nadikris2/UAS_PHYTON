from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import users,role

class RegistrationForm(FlaskForm):
      id = StringField('id', validators=[DataRequired()])
      name = StringField('name', validators=[DataRequired()])
      email = StringField('Email', validators=[DataRequired(), Email()])
      roleID = StringField('roleID', validators=[DataRequired()])
      password = PasswordField('password', validators=[DataRequired(),EqualTo('confirm_password')])

