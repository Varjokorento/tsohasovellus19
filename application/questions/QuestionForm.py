from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, validators, HiddenField

class QuestionForm(FlaskForm):
    question = TextAreaField("question", [validators.required()])
    answer = TextAreaField("answer")
    difficulty = IntegerField("difficulty", [validators.NumberRange(1, 10)])
    course_id = HiddenField()
    class Meta:
        csrf = False