from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from application.comments.CommentForm import CommentForm
from application.models.models import Comment

@app.route("/comment/<course_id>", methods=["POST"])
@login_required
def comment_form(course_id):
    return render_template("comments/addcomment.html", form = CommentForm(), course_id = course_id)


@app.route("/comment/new_comment", methods=["POST"])
@login_required
def new_comment():
    form = CommentForm(request.form)

    if not form.validate():
        return render_template("comments/addcomment.html", form = form)

    print(form.course_id.data)    

    t = Comment(form.text.data, form.grade.data, form.workload.data, form.course_id.data)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/comment/delete/<comment_id>", methods=["POST"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    db.session().delete(comment)
    db.session().commit()
    return redirect(url_for("courses_index"))


