from app import db

class User(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False)
class Course(db.model):
    id = db.column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    
