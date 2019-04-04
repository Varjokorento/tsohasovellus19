from application import db
from sqlalchemy.sql import text


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

    @staticmethod
    def find_comments(course_id):
        stmt = text("SELECT Comment.id, Comment.text, Comment.grade, Comment.workload FROM Comment"
                    " WHERE (Comment.course_id = :course_id)").params(course_id = course_id)
        res = db.engine.execute(stmt)
        return res

    @staticmethod 
    def find_questions(course_id):
        stmt = text("SELECT Question.id, Question.question, Question.answer, Question.difficulty FROM Question"
                    " WHERE (Question.course_id = :course_id)").params(course_id = course_id)
        res = db.engine.execute(stmt)
        print(res)
        return res
        

    @staticmethod
    def course_by_grade():
        stmt = text("SELECT Course.name, AVG(Comment.grade) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "avg":row[1]})
        return response


    @staticmethod
    def course_by_workload():
        stmt = text("SELECT Course.name, AVG(Comment.workload) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "avgworkload":row[1]})
        return response

    @staticmethod 
    def course_by_ects():
        stmt = text("Select Course.name, (Course.ects/AVG(Comment.workload)) from Course JOIN Comment on course.id = Comment.course_id GROUP BY Course.name, Course.ects")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0], "ects":row[1]})
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