# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    travel_style = SelectField('Travel Style', choices=[('adventurous', 'Adventurous'), ('relaxed', 'Relaxed')], validators=[DataRequired()])
    prefers_crowds = SelectField('Prefer Crowds?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    likes_culture = SelectField('Enjoy Culture?', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class DashboardForm(FlaskForm):
    preference = SelectField(
        'Travel Preference',
        choices=[
            ('Adventure', 'Adventure'),
            ('Mountains', 'Mountains'),
            ('Calm/Nature', 'Calm/Nature'),
            ('Beaches', 'Beaches'),
            ('Wildlife', 'Wildlife'),
            ('Culture/History', 'Culture/History'),
            ('Spiritual', 'Spiritual'),
        ],
        validators=[DataRequired()]
    )
    days = IntegerField('Number of days', validators=[DataRequired(), NumberRange(min=1, max=30)])
    submit = SubmitField('Get Recommendations')


class FeedbackForm(FlaskForm):
    feedback = TextAreaField('Your feedback', validators=[Length(max=500)])
    submit = SubmitField('Submit Feedback')
