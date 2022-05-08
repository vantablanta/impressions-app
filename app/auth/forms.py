from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, EqualTo
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired()])
    email = EmailField('Enter Email', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])  
    
    submit = SubmitField('Submit')
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
     email = EmailField('Enter Email', validators=[DataRequired()])
     password = PasswordField('Enter Password',validators=[DataRequired()] )
     remember = BooleanField('Remember me')
     submit = SubmitField('Submit')
