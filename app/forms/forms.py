from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AssetUploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices = [('image','Image')], validators=[DataRequired()])
    file = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')
    

class AssetGetForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')