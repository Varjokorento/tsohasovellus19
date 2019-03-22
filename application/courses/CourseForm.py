from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, validators

class CourseForm(FlaskForm):
    name = StringField("name", [validators.required()])
    description = TextAreaField("description", [validators.required()])
    core = BooleanField("core")
    class Meta:
        csrf = False