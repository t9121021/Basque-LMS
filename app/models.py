from app import db
<<<<<<< HEAD
from datetime import datetime
=======
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
>>>>>>> a35faf2204c99246513cf9499fe3e334e4f456a7

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20)) 
class Course(db.model):
    id = db.column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    
