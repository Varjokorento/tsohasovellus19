from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, validators

class CourseForm(FlaskForm):
    name = StringField("name", [validators.required()])
    description = TextAreaField("description", [validators.required()])
    core = BooleanField("core")
    ects = IntegerField("ects")
    class Meta:
        csrf = False