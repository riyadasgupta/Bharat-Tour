from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

from models import db, User

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize extensions
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register all blueprints AFTER initializing extensions
from routes.auth import auth_bp
from routes.planner import planner_bp
from routes.user import user_bp

app.register_blueprint(auth_bp)
app.register_blueprint(planner_bp)
app.register_blueprint(user_bp)

# Create the DB
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
