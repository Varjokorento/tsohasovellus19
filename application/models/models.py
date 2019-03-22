from application import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable= False)
    description = db.Column(db.String(10000), nullable=False)
    core = db.Column(db.Boolean, nullable=False)
    likes = db.Column(db.Integer, nullable=True)
    dislikes = db.Column(db.Integer, nullable=True)

    def __init__(self, name, description, core):
        self.name= name
        self.description = description
        self.core = core
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