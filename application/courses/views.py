from application import app, db, login_required
from flask import render_template, request, redirect, url_for
from application.models.models import Course, Comment, Question
from application.courses.CourseForm import CourseForm
from sqlalchemy.sql import text

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/course", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/course/showcourse/<course_id>", methods=["POST"])
def show_course(course_id):
    course = Course.query.get(course_id)
    return render_template("courses/showcourse.html", course = course)    

@app.route("/course/showcourse/<course_id>/showcomments", methods=["POST", "GET"])
def show_course_comments(course_id):
    page = request.args.get('page', 1, type=int)
    comments = Comment.query.filter_by(course_id=course_id).order_by(Comment.grade.desc()).paginate(page, 1, False)
    next_url = url_for('show_course_comments', course_id=course_id, page=comments.next_num) \
        if comments.has_next else None
    prev_url = url_for('show_course_comments', course_id=course_id,  page=comments.prev_num) \
        if comments.has_prev else None
    return render_template("courses/coursecomments.html", course_id= course_id, comments = comments.items,
    next_url= next_url, prev_url=prev_url)    

@app.route("/courses/showcourse/<course_id>/showquestions", methods=["POST", "GET"])
def show_course_questions(course_id):
    page = request.args.get('page', 1, type=int)
    questions = Question.query.filter_by(course_id=course_id).paginate(page, 1, False)
    next_url = url_for('show_course_questions', course_id=course_id, page=questions.next_num) \
        if questions.has_next else None
    prev_url = url_for('show_course_questions', course_id=course_id,  page=questions.prev_num) \
        if questions.has_prev else None
    return render_template("courses/coursequestions.html", course_id= course_id, questions = questions.items,
    next_url= next_url, prev_url=prev_url)    

@app.route("/course/new/")
@login_required(role="S")
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/course/", methods=["POST"])
def courses_create():
    form = CourseForm(request.form)
    if not form.validate():
        return render_template("/courses/new.html", form = form)
    t = Course(form.name.data, form.description.data, form.core.data, form.ects.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/updateinfo/<course_id>/", methods=["POST"])
@login_required(role="S")
def courses_update(course_id): 
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

@app.route("/course/taken<course_id><student_id>", methods=["POST"])
def mark_course_as_taken(course_id, student_id):
    stmt = text("INSERT INTO Course_Student(course_id, student_id) VALUES(:course_id, :student_id)").params(course_id=course_id, student_id=student_id)
    db.session().execute(stmt)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/course/mycourse/<student_id>")
def show_my_courses(student_id):
    stmt = text("SELECT DISTINCT Course.name FROM COURSE_STUDENT JOIN COURSE ON Course.id = Course_Student.course_id WHERE student_id = :student_id ").params(student_id=student_id)
    res = db.engine.execute(stmt)
    response = []
    for row in res:
        response.append({"name":row[0]})
    return render_template("courses/mycourses.html", courses = response)


@app.route("/course/update/", methods=["POST"])
@login_required(role="S")
def course_update():
    form = CourseForm(request.form)
    course = Course.query.get(form.course_id.data)
    if not form.validate():
        return render_template("/course/new.html", form = form)
    course.name = form.name.data
    course.description = form.description.data
    course.core = form.core.data
    course.ects = form.ects.data    
    db.session().commit()
    return redirect(url_for("courses_index"))

@app.route("/course/delete/<course_id>/", methods=["POST"])
@login_required(role="A")
def course_delete(course_id):
    course = Course.query.get(course_id)
    stmt = text("DELETE FROM Comment WHERE Comment.course_id = :course_id").params(course_id=course_id)
    db.session().execute(stmt)
    db.session().delete(course)
    db.session().commit()
    return redirect(url_for("courses_index"))
 