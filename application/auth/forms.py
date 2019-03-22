from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = TextAreaField("name", [validators.required()])
    username = TextAreaField("username", [validators.required()])
    password = PasswordField("password", [validators.required()])

    class Meta:
        csrf = False        