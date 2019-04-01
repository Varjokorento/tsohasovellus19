from application import app, db
from flask import render_template, request, redirect, url_for
from application.comments.CommentForm import CommentForm
from application.models.models import Course


@app.route("/coursestatistics", methods=["GET"])
def course_statistics():
    return render_template("statistics/coursestatistics.html", 
    courses_by_ects=Course.course_by_ects(), 
    courses_by_workload=Course.course_by_workload(), 
    courses_by_grade=Course.course_by_grade())


