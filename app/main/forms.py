from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Enter Name', validators=[DataRequired()])
    email = EmailField('Enter Email', validators=[DataRequired()])
    password = PasswordField('Enter Password',validators=[DataRequired()] )
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired()] )
    submit = SubmitField('Submit')

