import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///travel.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
