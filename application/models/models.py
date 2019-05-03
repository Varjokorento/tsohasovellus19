from application import db
from sqlalchemy.sql import text


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable= False)
    description = db.Column(db.String(500), nullable=False)
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

    @staticmethod
    def course_by_grade():
        stmt = text("SELECT Course.name, AVG(Comment.grade) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "avg":round(row[1],2)})
        return response


    @staticmethod
    def course_by_workload():
        stmt = text("SELECT Course.name, AVG(Comment.workload) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "avgworkload":round(row[1], 2)})
        return response

    @staticmethod 
    def course_by_ects():
        stmt = text("Select Course.name, (AVG(Comment.workload)/Course.ects) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name, Course.ects")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "ects":round(row[1],2)})
        return response

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable= False)
    grade = db.Column(db.Integer, nullable= False)
    workload = db.Column(db.Integer, nullable= False)
    course_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, text, grade, workload, course_id):
        self.text = text
        self.grade = grade
        self.workload = workload
        self.course_id = course_id

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(10), nullable=False)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role    

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000), nullable= False)
    answer = db.Column(db.String(1000), nullable= True)
    difficulty = db.Column(db.Integer, nullable= True)
    course_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, question, answer, difficulty, course_id):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.course_id = course_id

class UserRole(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    roleName= db.Column(db.String(10), nullable=False)

    def __init__(self, roleName):
        self.roleName = roleName

class CourseStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    __table_args__ = (db.UniqueConstraint('course_id', 'student_id', name='_student_course_uc'), )
    def __init__(self, course_id, student_id):
        self.course_id = course_id
        self.student_id = student_id