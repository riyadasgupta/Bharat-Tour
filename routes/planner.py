from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from utils.ai_recommend import get_recommendations, generate_itinerary, generate_pdf
from flask import send_file

planner_bp = Blueprint('planner', __name__)

@planner_bp.route('/')
def home():
    return render_template('index.html')

@planner_bp.route('/plan', methods=['GET', 'POST'])
@login_required
def plan():
    if request.method == 'POST':
        preferences = request.form.to_dict()
        recommendations = get_recommendations(preferences)
        return render_template('recommendations.html', recommendations=recommendations, days=preferences.get("days", 5))
    return render_template('planner.html')


@planner_bp.route('/itinerary/<destination>/<int:days>')
def itinerary(destination, days):
    itinerary_data = generate_itinerary(destination, days)
    return render_template('itinerary.html', itinerary=itinerary_data, destination=destination, days=days)

@planner_bp.route('/download/<destination>/<int:days>')
def download_itinerary(destination, days):
    itinerary_data = generate_itinerary(destination, days)
    pdf_path = generate_pdf(destination, itinerary_data)
    if pdf_path:
        return send_file(pdf_path, as_attachment=True)
    return "PDF generation failed", 500
