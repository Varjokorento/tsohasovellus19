from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField

class CommentForm(FlaskForm):
    text = TextAreaField("text")
    grade = IntegerField("grade")
    workload = IntegerField("workload")
    class Meta:
        csrf = False