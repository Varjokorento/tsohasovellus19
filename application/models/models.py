from application import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable= False)
    description = db.Column(db.String(10000), nullable=False)
    core = db.Column(db.Boolean, nullable=False)
    ects = db.Column(db.Integer, nullable=True)
    likes = db.Column(db.Integer, nullable=True)
    dislikes = db.Column(db.Integer, nullable=True)

    def __init__(self, name, description, core, ects):
        self.name= name
        self.description = description
        self.core = core
        self.ects = ects
        self.likes= 0
        self.dislikes =0

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable= False)
    grade = db.Column(db.Integer, nullable= False)
    workload = db.Column(db.Integer, nullable= False)
    
    def __init__(self, text, grade, workload):
        self.text = text
        self.grade = grade
        self.workload = workload

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True