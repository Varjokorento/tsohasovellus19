from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, validators, HiddenField

class CommentForm(FlaskForm):
    text = TextAreaField("text", [validators.Length(min=10), validators.required()])
    grade = IntegerField("grade", [validators.required()])
    workload = IntegerField("workload", [validators.required()])
    course_id = HiddenField()
    class Meta:
        csrf = False