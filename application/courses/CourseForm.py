from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, validators, HiddenField

class CourseForm(FlaskForm):
    name = StringField("name", [validators.Length(min=3, max=100), validators.required()])
    description = TextAreaField("description", [validators.Length(min=3, max=500), validators.required()])
    core = BooleanField("core", [validators.required()])
    ects = IntegerField("ects", [validators.NumberRange(1, 60)])
    course_id = HiddenField()
    class Meta:
        csrf = False