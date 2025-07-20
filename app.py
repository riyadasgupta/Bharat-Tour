from flask import Flask, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import db, User, Recommendation
from forms import RegistrationForm, LoginForm, DashboardForm, FeedbackForm
from config import Config
from recommendations import generate_itinerary_by_preference  # Custom recommendation logic

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter(
            (User.email == form.email.data) | (User.username == form.username.data)
        ).first()
        if existing_user:
            flash('User with this email or username already exists.', 'danger')
            return render_template('register.html', form=form)
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password,
            travel_style=form.travel_style.data,
            prefers_crowds=form.prefers_crowds.data,
            likes_culture=form.likes_culture.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    form = DashboardForm()
    if form.validate_on_submit():
        session['preference'] = form.preference.data
        session['days'] = form.days.data
        return redirect(url_for('recommendation'))
    return render_template('dashboard.html', form=form, username=session.get('username'))

@app.route('/recommendation')
def recommendation():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))

    preference = session.get('preference', 'Adventure')
    days = session.get('days', 7)
    rec = generate_itinerary_by_preference(preference, days)
    form = FeedbackForm()
    return render_template(
        'itinerary.html',
        rec=rec,
        itinerary_list=rec['itinerary'],
        username=session.get('username'),
        message=f"Here's a {preference.lower()} itinerary for you!",
        form=form
    )

@app.route('/itinerary/<int:rec_id>', methods=['GET', 'POST'])
def itinerary(rec_id):
    if 'user_id' not in session:
        flash('Please log in to view itineraries.', 'warning')
        return redirect(url_for('login'))

    rec = Recommendation.query.get_or_404(rec_id)
    if rec.user_id != session['user_id']:
        flash('You do not have permission to view this itinerary.', 'danger')
        return redirect(url_for('dashboard'))

    form = FeedbackForm()
    if form.validate_on_submit():
        feedback_text = form.feedback.data
        flash('Thank you for your feedback!', 'success')
        # Optional: Save or process feedback here
        return redirect(url_for('dashboard'))

    itinerary_list = rec.itinerary.split('\n')
    return render_template(
        'itinerary.html',
        form=form,
        rec=rec,
        itinerary_list=itinerary_list,
        username=session.get('username')
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
