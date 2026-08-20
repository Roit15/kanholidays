import json
import random

# Load current
with open('data/destinations.json', 'r') as f:
    data = json.load(f)

# Hardcoded data for 33 destinations
generic_highlights = ["Stunning Natural Landscapes", "Cultural & Heritage Sites", "Local Cuisine & Dining", "Guided City Tours", "Leisure & Shopping", "Comfortable Transfers"]

highlights_dict = {
    "bali": ["Ubud Monkey Forest", "Tanah Lot Temple Sunset", "Nusa Penida Day Trip", "Tegallalang Rice Terraces", "Balinese Spa Experience"],
    "dubai": ["Desert Safari with BBQ", "Burj Khalifa 124th Floor", "Dubai Mall & Fountain Show", "Marina Dhow Cruise", "Gold Souk Shopping"],
    "kashmir": ["Dal Lake Shikara Ride", "Gulmarg Gondola", "Pahalgam Betaab Valley", "Sonamarg Glaciers", "Mughal Gardens"],
    "maldives": ["Luxury Resort Stay", "Snorkeling & Diving", "Sunset Dolphin Cruise", "Private Beach Dinner", "Water Sports"],
    "mauritius": ["Chamarel Seven Coloured Earths", "Ile aux Cerfs Island", "Black River Gorges", "Port Louis Central Market", "Catamaran Cruise"],
    "europe": ["Eiffel Tower in Paris", "Swiss Alps Excursion", "Rome Colosseum", "Venice Gondola Ride", "Amsterdam Canals"],
    "thailand": ["Bangkok Grand Palace", "Phuket Phi Phi Islands", "Pattaya Coral Island", "Chiang Mai Temples", "Floating Markets"]
}

best_time_dict = {
    "bali": "April – October",
    "dubai": "November – March",
    "kashmir": "March – August",
    "maldives": "November – April",
    "mauritius": "May – December",
    "europe": "May – September",
    "thailand": "November – April"
}

for dest in data:
    slug = dest['slug']
    dest['highlights'] = highlights_dict.get(slug, generic_highlights)
    # Domestic (India) default vs International default
    if slug in ["kashmir", "ladakh", "himachal-pradesh", "uttarakhand", "spiti", "rajasthan", "meghalaya", "sikkim", "andaman", "kerala", "goa", "coorg", "arunachal-pradesh", "varanasi", "odisha"]:
        default_time = "October – March" 
    else:
        default_time = "Varies by season"
        
    dest['best_time'] = best_time_dict.get(slug, default_time)

with open('data/destinations.json', 'w') as f:
    json.dump(data, f, indent=4)
    
print("Added highlights and best_time to data/destinations.json")
