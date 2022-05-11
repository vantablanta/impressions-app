from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    body = TextAreaField('Leave a comment', validators = [DataRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators = [DataRequired()])
    category = StringField('Pitch Category', validators = [DataRequired()])   
    body = TextAreaField('Pitch', validators = [DataRequired()])
    submit = SubmitField('Submit')