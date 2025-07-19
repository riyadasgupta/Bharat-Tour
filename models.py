# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Create a database object for ORM

class User(db.Model):
    __tablename__ = 'user'  # Name of table in database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # Personalization fields:
    travel_style = db.Column(db.String(20))      # 'adventurous', 'relaxed', etc.
    prefers_crowds = db.Column(db.String(5))     # 'yes' or 'no'
    likes_culture = db.Column(db.String(5))      # 'yes' or 'no'

class Recommendation(db.Model):
    __tablename__ = 'recommendation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    hotels = db.Column(db.String(250), nullable=False)
    itinerary = db.Column(db.Text, nullable=False)
    user = db.relationship('User', backref=db.backref('recommendations', lazy=True))
