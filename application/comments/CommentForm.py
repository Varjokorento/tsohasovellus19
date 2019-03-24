from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, validators

class CommentForm(FlaskForm):
    text = TextAreaField("text", [validators.Length(min=10), validators.required()])
    grade = IntegerField("grade", [validators.required()])
    workload = IntegerField("workload", [validators.required()])
    class Meta:
        csrf = False