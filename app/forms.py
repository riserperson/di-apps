from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class AcrolistForm(FlaskForm):
    doc = FileField(u'Text File')
#    use_parens = BooleanField('Try to grab acronym definitons preceding acronyms enclosed in parentheses (still imperfect).')
    submit = SubmitField('Upload')
