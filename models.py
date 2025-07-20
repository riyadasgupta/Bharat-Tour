from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'  # Explicitly set table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)

    # Personalization fields
    travel_style = db.Column(db.String(20))       # 'adventurous', 'relaxed', etc.
    prefers_crowds = db.Column(db.String(5))       # 'yes' or 'no'
    likes_culture = db.Column(db.String(5))        # 'yes' or 'no'

    # Relationship
    recommendations = db.relationship('Recommendation', backref='user', lazy=True)

class Recommendation(db.Model):
    __tablename__ = 'recommendation'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    place = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    hotels = db.Column(db.String(250), nullable=False)
    itinerary = db.Column(db.Text, nullable=False)  # Can be plain text or JSON
