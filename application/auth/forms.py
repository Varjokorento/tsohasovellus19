from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = TextAreaField("name", [validators.required(), validators.Length(min=3, max=100)])
    username = TextAreaField("username", [validators.required(), validators.Length(min=3, max=100)])
    password = PasswordField("password", [validators.required(), validators.Length(min=6, max=50)])

    class Meta:
        csrf = False        