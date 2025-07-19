import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bharat_tours.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
