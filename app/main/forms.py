from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    name = StringField('Enter name', validators=[DataRequired])
    email = EmailField('Enter email', validators=[DataRequired])
    password = PasswordField('Enter Password',validators=[DataRequired] )
    password = PasswordField('Confirm Password',validators=[DataRequired] )
    submit = SubmitField('Enter Password',validators=[DataRequired] )

