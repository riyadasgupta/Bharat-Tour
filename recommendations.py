# recommendations.py

PLACES = {
    'Andhra Pradesh': {
        'name': 'Andhra Pradesh',
        'cuisine': 'Pulihora',
        'hotels': ['The Park Visakhapatnam', 'Novotel Visakhapatnam Varun Beach'],
        'activities': [
            'Visit Araku Valley',
            'Explore Borra Caves',
            'Relax at Rishikonda Beach',
            'Tour Simhachalam Temple'
        ]
    },
    'Arunachal Pradesh': {
        'name': 'Arunachal Pradesh',
        'cuisine': 'Thukpa',
        'hotels': ['Tawang Resort', 'Hotel Gakyi'],
        'activities': [
            'Explore Tawang Monastery',
            'Visit Ziro Valley',
            'See Sela Pass',
            'Trek Namdapha National Park'
        ]
    },
    'Assam': {
        'name': 'Assam',
        'cuisine': 'Assamese Thali',
        'hotels': ['Radisson Blu Guwahati', 'Hotel Brahmaputra Ashok'],
        'activities': [
            'Safari in Kaziranga National Park',
            'Visit Majuli Island',
            'Explore Kamakhya Temple',
            'Boat on Umananda Island'
        ]
    },
    'Bihar': {
        'name': 'Bihar',
        'cuisine': 'Litti Chokha',
        'hotels': ['Hotel Maurya', 'The Panache'],
        'activities': [
            'Visit Mahabodhi Temple (Bodh Gaya)',
            'Explore Nalanda Ruins',
            'Tour Rajgir Hot Springs',
            'See Vikramshila University'
        ]
    },
    'Chhattisgarh': {
        'name': 'Chhattisgarh',
        'cuisine': 'Chana Samosa',
        'hotels': ['Hotel Babylon Inn', 'Hotel Mayura Raipur'],
        'activities': [
            'Visit Chitrakote Falls',
            'Explore Bhuteshwar Temple',
            'Safari at Barnawapara Sanctuary',
            'Spot wildlife in Kanger Valley'
        ]
    },
    'Goa': {
        'name': 'Goa',
        'cuisine': 'Goan Fish Curry',
        'hotels': ['Taj Exotica', 'The Leela Goa'],
        'activities': [
            'Relax at Baga Beach',
            'Tour Old Goa Churches',
            'See Dudhsagar Waterfalls',
            'Visit Anjuna Market'
        ]
    },
    'Gujarat': {
        'name': 'Gujarat',
        'cuisine': 'Dhokla',
        'hotels': ['Hyatt Ahmedabad', 'The Fern Vadodara'],
        'activities': [
            'Visit Rann of Kutch',
            'Explore Gir Forest',
            'Tour Sabarmati Ashram',
            'See Modhera Sun Temple'
        ]
    },
    'Haryana': {
        'name': 'Haryana',
        'cuisine': 'Bajra Khichdi',
        'hotels': ['The Westin Gurgaon', 'ITC Grand Bharat'],
        'activities': [
            'Relax at Sohna Hot Springs',
            'Visit Kurukshetra',
            'See Sultanpur Bird Sanctuary',
            'Tour Morni Hills'
        ]
    },
    'Himachal Pradesh': {
        'name': 'Himachal Pradesh',
        'cuisine': 'Siddu',
        'hotels': ['Clarkes Hotel Shimla', 'Snow Valley Resort Manali'],
        'activities': [
            'Mall Road Shimla',
            'Rohtang Pass',
            'Manali Solang Valley',
            'McLeod Ganj Tour'
        ]
    },
    'Jharkhand': {
        'name': 'Jharkhand',
        'cuisine': 'Thekua',
        'hotels': ['Hotel Capitol Hill', 'The Sonnet Ranchi'],
        'activities': [
            'Hundru Falls',
            'Patratu Valley',
            'Rock Garden Ranchi',
            'Jagannath Temple'
        ]
    },
    'Karnataka': {
        'name': 'Karnataka',
        'cuisine': 'Bisi Bele Bath',
        'hotels': ['ITC Gardenia', 'The Ritz-Carlton Bangalore'],
        'activities': [
            'Mysore Palace',
            'Coorg Coffee Estates',
            'Hampi Ruins',
            'Cubbon Park Visit'
        ]
    },
    'Kerala': {
        'name': 'Kerala',
        'cuisine': 'Kerala Sadya',
        'hotels': ['Taj Kovalam', 'The Leela Ashtamudi'],
        'activities': [
            'Cruise Alleppey Backwaters',
            'Trek Munnar Tea Gardens',
            'Relax at Kovalam Beach',
            'Explore Fort Kochi'
        ]
    },
    'Madhya Pradesh': {
        'name': 'Madhya Pradesh',
        'cuisine': 'Poha',
        'hotels': ['Radisson Bhopal', 'Sayaji Indore'],
        'activities': [
            'Khajuraho Temples',
            'Bhopal Lake',
            'Kanha Park Safari',
            'Sanchi Stupa'
        ]
    },
    'Maharashtra': {
        'name': 'Maharashtra',
        'cuisine': 'Vada Pav',
        'hotels': ['The Taj Mahal Palace', 'Trident Nariman Point'],
        'activities': [
            'Marine Drive',
            'Visit Elephanta Caves',
            'Ajanta & Ellora',
            'Sinhagad Fort'
        ]
    },
    'Manipur': {
        'name': 'Manipur',
        'cuisine': 'Eromba',
        'hotels': ['Classic Hotel Imphal', 'The Sangai Continental'],
        'activities': [
            'Loktak Lake',
            'Govindajee Temple',
            'Kangla Fort',
            'Keibul Lamjao Park'
        ],
    },
    'Meghalaya': {
        'name': 'Meghalaya',
        'cuisine': 'Jadoh',
        'hotels': ['Ri Kynjai', 'Polo Towers Shillong'],
        'activities': [
            'Nohkalikai Falls',
            'Mawsynram',
            'Living Root Bridges',
            'Umiam Lake'
        ]
    },
    'Mizoram': {
        'name': 'Mizoram',
        'cuisine': 'Bai',
        'hotels': ['Regency Aizawl', 'Chaltlang Lodge'],
        'activities': [
            'Reiek Mountain',
            'Solomon Temple',
            'Tamdil Lake',
            'Durtlang Hills'
        ]
    },
    'Nagaland': {
        'name': 'Nagaland',
        'cuisine': 'Smoked Pork Curry',
        'hotels': ['Japfü Kohima', 'Saramati Dimapur'],
        'activities': [
            'Kisama Heritage Village',
            'Kohima Museum',
            'Dzükou Valley Trek',
            'Tuophema Village'
        ]
    },
    'Odisha': {
        'name': 'Odisha',
        'cuisine': 'Pakhala Bhata',
        'hotels': ['Mayfair Bhubaneswar', 'Swosti Premium'],
        'activities': [
            'Puri Beach',
            'Konark Temple',
            'Chilika Lake',
            'Lingaraj Temple'
        ]
    },
    'Punjab': {
        'name': 'Punjab',
        'cuisine': 'Sarson da Saag & Makki di Roti',
        'hotels': ['JW Marriott Chandigarh', 'Hyatt Amritsar'],
        'activities': [
            'Golden Temple',
            'Jallianwala Bagh',
            'Wagah Border',
            'Patiala Qila Mubarak'
        ]
    },
    'Rajasthan': {
        'name': 'Rajasthan',
        'cuisine': 'Dal Baati Churma',
        'hotels': ['Taj Rambagh Palace', 'Leela Udaipur'],
        'activities': [
            'City Palace Jaipur',
            'Lake Pichola Udaipur',
            'Amber Fort',
            'Ranthambore Safari'
        ]
    },
    'Sikkim': {
        'name': 'Sikkim',
        'cuisine': 'Phagshapa',
        'hotels': ['Mayfair Spa Gangtok', 'Elgin Mount Pandim'],
        'activities': [
            'Tsongmo Lake',
            'Nathula Pass',
            'Rumtek Monastery',
            'Walk MG Road'
        ]
    },
    'Tamil Nadu': {
        'name': 'Tamil Nadu',
        'cuisine': 'Dosa & Coffee',
        'hotels': ['ITC Grand Chola', 'The Leela Chennai'],
        'activities': [
            'Meenakshi Temple',
            'Marina Beach',
            'Mahabalipuram',
            'Ooty Garden Walk'
        ]
    },
    'Telangana': {
        'name': 'Telangana',
        'cuisine': 'Hyderabadi Biryani',
        'hotels': ['Taj Falaknuma Palace', 'Park Hyatt Hyderabad'],
        'activities': [
            'Charminar',
            'Golconda Fort',
            'Hussain Sagar Lake',
            'Laad Bazaar'
        ]
    },
    'Tripura': {
        'name': 'Tripura',
        'cuisine': 'Mui Borok',
        'hotels': ['Hotel Rajdhani', 'Ginger Agartala'],
        'activities': [
            'Ujjayanta Palace',
            'Sepahijala Park',
            'Neermahal Palace',
            'Trishna Sanctuary'
        ]
    },
    'Uttar Pradesh': {
        'name': 'Uttar Pradesh',
        'cuisine': 'Tunday Kabab',
        'hotels': ['Taj Ganges Varanasi', 'ITC Mughal Agra'],
        'activities': [
            'Taj Mahal',
            'Sarnath',
            'Varanasi Ghats',
            'Lucknow Imambara'
        ]
    },
    'Uttarakhand': {
        'name': 'Uttarakhand',
        'cuisine': 'Aloo ke Gutke',
        'hotels': ['Naini Retreat', 'Ananda Himalayas'],
        'activities': [
            'Nainital Hills',
            'Rishikesh River Rafting',
            'Haridwar Ghats',
            'Corbett Park'
        ]
    },
    'West Bengal': {
        'name': 'West Bengal',
        'cuisine': 'Shorshe Ilish',
        'hotels': ['Oberoi Grand', 'ITC Sonar'],
        'activities': [
            'Victoria Memorial',
            'Sunderbans Safari',
            'Darjeeling Toy Train',
            'Howrah Bridge'
        ]
    },
    # Union Territories
    'Delhi': {
        'name': 'Delhi',
        'cuisine': 'Chole Bhature',
        'hotels': ['The Oberoi', 'ITC Maurya'],
        'activities': [
            'Red Fort',
            'Qutub Minar',
            'Lotus Temple',
            'India Gate'
        ]
    },
    'Puducherry': {
        'name': 'Puducherry',
        'cuisine': 'French Creole',
        'hotels': ['Palais de Mahe', 'Promenade'],
        'activities': [
            'Promenade Beach',
            'Auroville',
            'French Colony',
            'Paradise Beach'
        ]
    },
    'Ladakh': {
        'name': 'Ladakh',
        'cuisine': 'Thukpa',
        'hotels': ['Grand Dragon Ladakh', 'Ladakh Sarai'],
        'activities': [
            'Pangong Lake',
            'Magnetic Hill',
            'Leh Palace',
            'Nubra Valley'
        ]
    },
    'Jammu and Kashmir': {
        'name': 'Jammu and Kashmir',
        'cuisine': 'Rogan Josh',
        'hotels': ['Lalit Srinagar', 'Vivanta Dal View'],
        'activities': [
            'Dal Lake Tour',
            'Gulmarg Skiing',
            'Vaishno Devi',
            'Mughal Gardens'
        ]
    },
    'Andaman and Nicobar Islands': {
        'name': 'Andaman and Nicobar Islands',
        'cuisine': 'Seafood',
        'hotels': ['SeaShell Havelock', 'Barefoot Resort'],
        'activities': [
            'Radhanagar Beach',
            'Snorkeling Elephant Beach',
            'Ross Island',
            'Cellular Jail'
        ]
    },
    'Lakshadweep': {
        'name': 'Lakshadweep',
        'cuisine': 'Coconut Seafood Curry',
        'hotels': ['Agatti Island Resort', 'Kavaratti Island Resort'],
        'activities': [
            'Kavaratti Scuba Diving',
            'Minicoy Beach',
            'Bangaram Island',
            'Kalapeni Island'
        ]
    },
    'Chandigarh': {
        'name': 'Chandigarh',
        'cuisine': 'Rajma Chawal',
        'hotels': ['JW Marriott', 'Taj Chandigarh'],
        'activities': [
            'Rock Garden',
            'Sukhna Lake',
            'Rose Garden',
            'Capitol Complex'
        ]
    },
    'Dadra and Nagar Haveli and Daman and Diu': {
        'name': 'Dadra and Nagar Haveli and Daman and Diu',
        'cuisine': 'Portuguese Seafood',
        'hotels': ['Deltin Daman', 'Cidade de Diu'],
        'activities': [
            'Devka Beach',
            'Diu Fort',
            'Nani Daman',
            'Silvassa Tribal Museum'
        ]
    }
}

PREFERENCE_MAPPING = {
    "Adventure": ["Rajasthan", "Ladakh", "Sikkim", "Uttarakhand", "Goa"],
    "Mountains": ["Himachal Pradesh", "Uttarakhand", "Sikkim", "Nagaland", "Arunachal Pradesh"],
    "Calm/Nature": ["Kerala", "Meghalaya", "Goa", "Andaman and Nicobar Islands", "Lakshadweep"],
    "Beaches": ["Goa", "Kerala", "Andaman and Nicobar Islands", "Lakshadweep", "Puducherry", "Odisha"],
    "Wildlife": ["Madhya Pradesh", "Assam", "Chhattisgarh", "Jharkhand", "Karnataka"],
    "Culture/History": ["Uttar Pradesh", "Tamil Nadu", "Delhi", "Maharashtra", "West Bengal"],
    "Spiritual": ["Uttar Pradesh", "Varanasi", "Jammu and Kashmir", "Odisha"],
}

import random

def select_state_by_preference(preference):
    states = PREFERENCE_MAPPING.get(preference)
    if not states:
        return random.choice(list(PLACES.keys()))
    return random.choice(states)

def generate_itinerary_by_preference(preference, days):
    place_key = select_state_by_preference(preference)
    place = PLACES[place_key]
    activities = place.get('activities', [])
    if not activities:
        activities = [f"Explore the cultural wonders of {place['name']}"]
    itinerary = []
    for i in range(days):
        activity = activities[i % len(activities)]
        itinerary.append(f"Day {i + 1}: {activity} in {place['name']}")
    return {
        'place': place['name'],
        'cuisine': place['cuisine'],
        'hotels': ', '.join(place['hotels']),
        'itinerary': itinerary
    }
