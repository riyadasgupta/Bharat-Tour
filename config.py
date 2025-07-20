import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///travel.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
