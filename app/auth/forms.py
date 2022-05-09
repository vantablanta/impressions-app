from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError, BooleanField
from wtforms.validators import EqualTo, InputRequired
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField('Enter username', validators=[InputRequired()])
    email = EmailField('Enter Email', validators=[InputRequired()])
    password = PasswordField('Enter Password', validators=[InputRequired(),EqualTo('confirm_password',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',validators=[InputRequired()])  
    submit = SubmitField('Submit')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('There is an account with that email')

    def validate_username(self,name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
     email = EmailField('Enter Email', validators=[InputRequired()])
     password = PasswordField('Enter Password',validators=[InputRequired()] )
     remember = BooleanField('Remember me')
     submit = SubmitField('Submit')
