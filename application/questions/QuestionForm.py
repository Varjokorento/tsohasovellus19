from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, validators, HiddenField

class QuestionForm(FlaskForm):
    question = TextAreaField("question", [validators.Length(min=3, max=500), validators.required()])
    answer = TextAreaField("answer", [validators.Length(min=3, max=500), validators.required()])
    difficulty = IntegerField("difficulty", [validators.NumberRange(1, 10), validators.required()])
    course_id = HiddenField()
    class Meta:
        csrf = False