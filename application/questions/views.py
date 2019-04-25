from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.questions.QuestionForm import QuestionForm
from application.models.models import Question

@app.route("/question/<course_id>", methods=["POST"])
@login_required("S")
def question_form(course_id):
    return render_template("questions/addquestion.html", form = QuestionForm(), course_id = course_id)

@app.route("/question/new_question", methods=["POST"])
@login_required("S")
def new_question():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/addquestion.html", form = form)

    t = Question(form.question.data, form.answer.data, form.difficulty.data, form.course_id.data)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))