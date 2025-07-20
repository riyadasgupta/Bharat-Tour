import os

class Config:
<<<<<<< HEAD
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bharat_tours.db'
=======
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_dev_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///travel.db'
>>>>>>> 7496ed3 (initial commit)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
