from application import app, db
from flask import render_template, request, redirect, url_for
from application.models.models import Course
from application.courses.CourseForm import CourseForm
from sqlalchemy.sql import text

@app.route("/course", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/course/showcourse/<course_id>", methods=["POST"])
def show_course(course_id):
    course = Course.query.get(course_id)
    comments = Course.find_comments(course_id)
    return render_template("courses/showcourse.html", course = course, comments = comments)    

@app.route("/course/new/")
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/course/", methods=["POST"])
def courses_create():
    form = CourseForm(request.form)
    if not form.validate():
        return render_template("/course/new.html", form = form)
    t = Course(form.name.data, form.description.data, form.core.data, form.ects.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/updateinfo/<course_id>/", methods=["POST"])
def courses_update(course_id): 
    print("Here")
    print(course_id)
    course = Course.query.get(course_id)
    form = CourseForm(obj=course)
    return render_template("courses/update.html", form = form, course_id = course_id)   

@app.route("/course/like/<course_id>/", methods=["POST"])
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

@app.route("/course/update/", methods=["POST"])
def course_update():
    form = CourseForm(request.form)
    course = Course.query.get(form.course_id.data)
    if not form.validate():
        return render_template("/course/new.html", form = form)
    course.name = form.name.data
    course.description = form.name.description
    course.core = form.core.data
    course.ects = form.ects.data    
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/delete/<course_id>/", methods=["POST"])
def course_delete(course_id):
    course = Course.query.get(course_id)
    stmt = text("DELETE FROM Comment WHERE Comment.course_id = :course_id").params(course_id=course_id)
    db.session().execute(stmt)
    db.session().delete(course)
    db.session().commit()
    return redirect(url_for("courses_index"))
 