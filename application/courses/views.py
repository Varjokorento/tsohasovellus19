from application import app, db
from flask import render_template, request, redirect, url_for
from application.models.models import Course
from application.courses.CourseForm import CourseForm

@app.route("/course", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/course/new/")
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/course/", methods=["POST"])
def courses_create():
    form = CourseForm(request.form)
    if not form.validate():
        return render_template("/course/new/", form = form)
    t = Course(form.name.data, form.description.data, form.core.data, form.ects.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/<course_id>/", methods=["POST"])
def course_add_like(course_id):
    t = Course.query.get(course_id)
    t.likes = t.likes +1 
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/dislike/<course_id>/", methods=["POST"])
def course_add_dislike(course_id):
    t = Course.query.get(course_id)
    t.dislikes = t.dislikes +1 
    db.session().commit()
    return redirect(url_for("courses_index"))

 