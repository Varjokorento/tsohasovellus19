from application import app, db
from flask import render_template, request, redirect, url_for

@app.route("/comment/<course_id>", methods=["POST"])
def comment_add_comment(course_id):
    print(course_id)
    return render_template("comments/addcomment.html")
