from application import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable= False)
    description = db.Column(db.String(10000), nullable=False)
    core = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, description, core):
        self.name= name
        self.description = description
        self.core = core