from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    category = StringField('Enter Category', validators = [DataRequired()])
    comment = TextAreaField('Leave a comment', validators = [DataRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')