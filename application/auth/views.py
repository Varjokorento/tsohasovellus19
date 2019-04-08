from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.models.models import User 
from application.auth.forms import NewUserForm, LoginForm

@app.route("/auth/new_user", methods=["GET"]) 
def new_user_form():
    return render_template("auth/newuser.html", form = NewUserForm())

@app.route("/auth/new_user", methods=["POST"]) 
def create_new_user():
    form = NewUserForm(request.form)

    if not form.validate():
        return render_template("/comment/new_comment", form = form)

    t = User(form.name.data, form.username.data, form.password.data, "STD")
    print("NEW USER")
    print(t.role)
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))



@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    print(user.password)
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))   

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    