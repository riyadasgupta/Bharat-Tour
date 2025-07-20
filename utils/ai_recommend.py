import json
import os
from xhtml2pdf import pisa
from flask import render_template

def get_recommendations(preferences):
    theme = preferences.get('theme')
    if theme == 'culture':
        return [{'destination': 'Rajasthan', 'desc': 'Royal forts, haveli, rich heritage'}]
    elif theme == 'nature':
        return [{'destination': 'Kerala', 'desc': 'Hills, backwaters, and greenery'},
                {'destination': 'Himachal Pradesh', 'desc': 'Snow-capped mountains and valleys'}]
    elif theme == 'beaches':
        return [{'destination': 'Goa', 'desc': 'Beaches, seafood, and chill'}]
    elif theme == 'spiritual':
        return [{'destination': 'Uttarakhand', 'desc': 'Yoga, temples, and Ganga aarti'}]
    else:
        return [{'destination': 'Kerala', 'desc': 'God’s own country'}]

def generate_itinerary(destination, days=5):
    filepath = os.path.join("data", "places_data.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    places = data.get(destination, {}).get("cities", ["City 1", "City 2"])
    foods = data.get(destination, {}).get("foods", ["Local Dish 1", "Dish 2"])

    itinerary = []
    for i in range(int(days)):
        itinerary.append({
            "day": i + 1,
            "place": places[i % len(places)],
            "food": foods[i % len(foods)],
            "hotel": f"{destination} Stay #{i+1}"
        })

    return itinerary


def generate_pdf(destination, itinerary):
    html = render_template("pdf_template.html", destination=destination, itinerary=itinerary)
    filepath = f"static/itineraries/{destination}_itinerary.pdf"

    with open(filepath, "wb") as f:
        pisa_status = pisa.CreatePDF(html, dest=f)

    if pisa_status.err:
        return None
    return filepath
