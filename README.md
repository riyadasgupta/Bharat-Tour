BharatTour – AI-Powered Travel Planner for India 🇮🇳
BharatTour is an interactive, AI-enabled web application that provides personalized travel recommendations and dynamic itineraries for exploring India's rich culture, destinations, food, and festivals.

Built using Flask, Bootstrap, and SQLite, BharatTour is designed for wanderers, digital nomads, and global travelers who want a one-stop solution for exploring India based on their travel preferences.

Features:
1. User Registration & Login (with secure password hashing)

2. AI-Generated Itinerary Based on:

--> Travel duration

--> Interests (culture, food, adventure, nature)

3. Dynamic Recommendations with Local Cuisine and Hotels

4. Personalized Dashboard & Feedback System

5. Interactive, Responsive UI (Mobile Friendly)

6. PDF Itinerary Export built with xhtml2pdf

7. Admin-ready backend using Flask + SQLAlchemy

Technologies Used:
Backend: Python 3, Flask, Flask-WTF, Flask-Login

Database: SQLite + SQLAlchemy ORM

Frontend: HTML5, Jinja2, Bootstrap 5, CSS3

AI Logic: Rule-based recommendation system

PDF Generation: xhtml2pdf

Version Control: Git & GitHub

How It Works?
1. User registers and completes a travel preference form

2. Based on their interests and trip duration, AI suggests best Indian states & highlights

3. A detailed, day-wise itinerary is generated

4. Each day includes:

--> Tourist destinations

--> Recommended food

--> Suggested hotel/stay

5. Users can download the itinerary as a styled PDF or provide feedback

Project Setup:
1. Clone the Repo
bash
git clone https://github.com/riyadasgupta/Bharat-Tour.git
cd Bharat-Tour
2. Create a Virtual Environment
bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the App Locally
bash
python app.py
Open in your browser at: http://127.0.0.1:5000

Project Structure

Bharat-Tour/
├── app.py
├── config.py
├── models.py
├── forms.py
├── routes/
│   ├── auth.py
│   ├── planner.py
│   └── user.py
├── utils/
│   └── ai_recommend.py
├── templates/
├── static/
├── data/
│   └── places_data.json
├── requirements.txt
└── README.md

Future Plans
Integrate real-time weather and local events per region

Add Google Maps API for live place visuals

Add multi-language support (Hindi / Bengali / etc.)

OAuth Login with Google

Admin Dashboard for travel agency integration




