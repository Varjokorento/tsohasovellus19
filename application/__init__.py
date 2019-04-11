from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"    
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)


from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="STD"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            print(current_user) 
            print("I AM HERE")
            roles = current_user.roles()
            print(roles)
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "STD":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from application import views

from application.models import models
from application.courses import views
from application.questions import views
from application.comments import views
from application.statistics import views

from application.auth import views
from application.auth import models 

# kirjautuminen
from application.models.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

db.drop_all();

try: 
    db.create_all()
except:
    pass