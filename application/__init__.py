from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///models.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


from application import views

from application.models import models
from application.courses import views
from application.comments import views

db.create_all()
