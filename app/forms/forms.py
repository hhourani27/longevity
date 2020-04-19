from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, MultipleFileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class AssetUploadForm(FlaskForm) :
    collection = SelectField('Collection', choices=[], coerce=int, validators=[DataRequired()])
    format = SelectField('Format', choices=[], coerce=int, validators=[DataRequired()])
    files = MultipleFileField()
    submit = SubmitField('Submit')
    

class AssetGetForm(FlaskForm) :
    id = StringField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
class CollectionGetForm(FlaskForm) :
    
    def __init__(self, choices, default = None, *args, **kwargs):     
        if default is None :    
            collection = SelectField('Collection', choices=choices, coerce=int, validators=[DataRequired()])
        else : 
            collection = SelectField('Collection', choices=choices, default=default, coerce=int, validators=[DataRequired()])
        
        submit = SubmitField('Submit')
        
        self._unbound_fields = self._unbound_fields + [['collection', collection],['submit', submit]]
        
        super(CollectionGetForm, self).__init__(*args, **kwargs)