from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms import validators
from wtforms.fields.choices import SelectField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    category = StringField('Blog Category') 
    context = TextAreaField('Blog Content')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField('Comment title')
    comment = TextAreaField('Leave a comment')
    submit = SubmitField('Submit')