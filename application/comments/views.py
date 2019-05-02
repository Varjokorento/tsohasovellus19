from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.comments.CommentForm import CommentForm
from application.models.models import Comment

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/comment/<course_id>", methods=["POST"])
@login_required(role="S")
def comment_form(course_id):
    return render_template("comments/addcomment.html", form = CommentForm(), course_id = course_id)


@app.route("/comment/new_comment", methods=["POST"])
@login_required(role="S")
def new_comment():
    form = CommentForm(request.form)

    if not form.validate():
        return render_template("comments/addcomment.html", form = form)
    workload = int(form.workload.data) * int(form.time_in_weeks.data)
    t = Comment(form.text.data, form.grade.data, workload, form.course_id.data)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/comment/delete/<comment_id>", methods=["POST"])
@login_required(role="A")
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    db.session().delete(comment)
    db.session().commit()
    return redirect(url_for("courses_index"))


