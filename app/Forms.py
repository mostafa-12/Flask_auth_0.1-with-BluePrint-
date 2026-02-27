from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from .models import User
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')
    def validate(self, extra_validators = None):
        if not super().validate(extra_validators):
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("there is no user with this email")
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append("Wrong password")
            return False
        return True
class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm your password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('SignUp')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken, choose a different one")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken, choose a different one")