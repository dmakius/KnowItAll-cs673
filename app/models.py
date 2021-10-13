from app import db


# Define question table Schema
class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(129), unique=False, nullable=False)
    question = db.Column(db.String(129), unique=True, nullable=False)
    answer = db.Column(db.String(129), unique=True, nullable=False)
    option_1 = db.Column(db.String(129), unique=True, nullable=False)
    option_2 = db.Column(db.String(129), unique=True, nullable=False)
    option_3 = db.Column(db.String(129), unique=True, nullable=False)
