from app import db

#class ToDo stores the data received from the form to the database
class ToDo(db.Model):
    __tablename__ = 'ToDo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), index=True, unique=True)
    module_code = db.Column(db.String, index = True, unique = True)
    deadline = db.Column(db.Date())
    description = db.Column(db.String)
    status = db.Column(db.String)

    #initializes the databse
    def __init__(self,title, module_code, deadline, description, status):
        self.title = title
        self.module_code = module_code
        self.deadline = deadline
        self.description = description
        self.status = status


