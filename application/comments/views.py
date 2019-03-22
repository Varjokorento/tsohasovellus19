from application import app, db
from flask import render_template, request, redirect, url_for
from application.comments.CommentForm import CommentForm
from application.models.models import Comment

@app.route("/comment/<course_id>", methods=["POST"])
def comment_form(course_id):
    return render_template("comments/addcomment.html", form = CommentForm())

@app.route("/new_comment", methods=["POST"])
def new_comment():
    form = CommentForm(request.form)

    t = Comment(form.text.data, form.grade.data, form.workload.data)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))


