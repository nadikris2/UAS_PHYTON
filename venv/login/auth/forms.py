from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from venv.models import users,role

class RegistrationForm(FlaskForm):
      id = StringField('id', validators=[DataRequired()])
      name = StringField('name', validators=[DataRequired()])
      email = StringField('Email', validators=[DataRequired(), Email()])
      roleID = StringField('roleID', validators=[DataRequired()])
      password = PasswordField('password', validators=[DataRequired(),EqualTo('confirm_password')])
      submit = SubmitField('Register')

      def validate_email(self, field):
        if users.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

      def validate_id(self, field):
        if users.query.filter_by(id=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
      id = StringField('id', validators=[DataRequired()])
      email = StringField('Email', validators=[DataRequired(), Email()])
      password = PasswordField('Password', validators=[DataRequired()])
      submit = SubmitField('Login')
