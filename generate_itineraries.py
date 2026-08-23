import json
import random

# Core highlights for each destination to generate realistic-looking itineraries
highlights = {
    "bali": ["Ubud Monkey Forest & Rice Terraces", "Tanah Lot Temple Sunset", "Nusa Penida Island Tour", "Seminyak Beach Leisure", "Uluwatu Temple & Kecak Dance", "Water Sports at Tanjung Benoa"],
    "dubai": ["Desert Safari & BBQ Dinner", "Burj Khalifa At The Top", "Dubai Mall & Aquarium", "Dubai Marina Cruise", "Abu Dhabi Grand Mosque Tour", "Miracle Garden & Global Village"],
    "maldives": ["Resort Check-in & Beach Leisure", "Snorkeling & Water Sports", "Sunset Dolphin Cruise", "Private Sandbank Picnic", "Spa & Wellness Day", "Leisure Day"],
    "kashmir": ["Srinagar Dal Lake Shikara Ride", "Gulmarg Gondola Ride", "Pahalgam Valley Tour", "Sonamarg Glaciers", "Mughal Gardens Visit", "Local Market Shopping"],
    "mauritius": ["North Island Tour & Port Louis", "South Island & Chamarel", "Ile Aux Cerfs Water Sports", "Catamaran Cruise", "Casela Nature Park", "Leisure Beach Day"],
    "europe": ["Paris City Tour & Eiffel Tower", "Swiss Alps & Jungfraujoch", "Rome Colosseum & Vatican", "Venice Gondola Ride", "Amsterdam Canal Cruise", "London Eye & Thames", "Rhine Falls Visit", "Black Forest Tour", "Leisure & Shopping"],
    "greece": ["Athens Acropolis Tour", "Santorini Oia Sunset", "Mykonos Beach Day", "Volcano & Hot Springs Cruise", "Temple of Poseidon", "Island Hopping"],
    "switzerland": ["Zurich City Tour", "Mt. Titlis Cable Car", "Interlaken Lakes", "Lucerne Chapel Bridge", "Glacier Express Journey", "Geneva Jet d'Eau"],
    "russia": ["Moscow Red Square", "Kremlin Tour", "St. Petersburg Hermitage", "Peterhof Palace", "Metro Stations Tour", "Nevsky Prospect Walk"],
    "ladakh": ["Leh Palace & Shanti Stupa", "Pangong Lake Trip", "Nubra Valley & Khardung La", "Magnetic Hill & Sangam", "Hemis Monastery", "Local Bazaar"],
    "himachal-pradesh": ["Shimla Mall Road", "Manali Rohtang Pass", "Solang Valley Adventure", "Dharamshala McLeod Ganj", "Dalhousie Khajjiar", "Kullu River Rafting"],
    "uttarakhand": ["Nainital Lake Tour", "Jim Corbett Safari", "Mussoorie Kempty Falls", "Rishikesh Ganga Aarti", "Auli Ropeway", "Haridwar Temples"],
    "spiti": ["Kaza Town Tour", "Key Monastery", "Chandratal Lake", "Komic & Langza Villages", "Kunzum Pass", "Tabo Monastery"],
    "rajasthan": ["Jaipur Amber Fort", "Udaipur Lake Pichola", "Jodhpur Mehrangarh", "Jaisalmer Desert Safari", "Pushkar Lake", "Bikaner Fort"],
    "meghalaya": ["Shillong Peak & Ward's Lake", "Cherrapunjee Waterfalls", "Dawki River Boat Ride", "Mawlynnong Cleanest Village", "Living Root Bridges", "Nohkalikai Falls"],
    "sikkim": ["Gangtok MG Marg", "Tsomgo Lake & Baba Mandir", "Nathu La Pass", "Pelling Pemayangtse Monastery", "Ravangla Buddha Park", "Namchi Char Dham"],
    "andaman": ["Port Blair Cellular Jail", "Havelock Radhanagar Beach", "Neil Island Tour", "Ross Island Ruins", "Elephant Beach Snorkeling", "Baratang Limestone Caves"],
    "kerala": ["Munnar Tea Gardens", "Alleppey Houseboat Cruise", "Thekkady Periyar Safari", "Kochi Chinese Fishing Nets", "Kovalam Beach", "Wayanad Waterfalls"],
    "goa": ["North Goa Beaches", "South Goa Temples & Churches", "Dudhsagar Waterfalls", "Spice Plantation Tour", "Mandovi River Cruise", "Anjuna Flea Market"],
    "coorg": ["Abbey Falls", "Raja's Seat Sunset", "Dubare Elephant Camp", "Talakaveri", "Coffee Plantation Tour", "Namdroling Monastery"],
    "arunachal-pradesh": ["Tawang Monastery", "Sela Pass", "Bum La Pass", "Ziro Valley", "Dirang Dzong", "Nuranang Falls"],
    "varanasi": ["Ganga Aarti at Dashashwamedh", "Kashi Vishwanath Temple", "Sarnath Stupa", "Morning Boat Ride", "Ramnagar Fort", "Banaras Hindu University"],
    "odisha": ["Puri Jagannath Temple", "Konark Sun Temple", "Chilika Lake Dolphins", "Bhubaneswar Lingaraj Temple", "Udayagiri Caves", "Chandipur Beach"],
    "vietnam": ["Hanoi Old Quarter", "Halong Bay Cruise", "Ho Chi Minh City Tour", "Cu Chi Tunnels", "Hoi An Lantern Town", "Mekong Delta Boat Ride"],
    "thailand": ["Bangkok Grand Palace", "Phuket Phi Phi Islands", "Pattaya Coral Island", "Chiang Mai Temples", "Krabi Four Islands", "Ayutthaya Ruins"],
    "japan": ["Tokyo Skytree & Shibuya", "Kyoto Temples & Shrines", "Osaka Castle & Dotonbori", "Mt. Fuji & Hakone", "Nara Deer Park", "Hiroshima Peace Park"],
    "sri-lanka": ["Colombo City Tour", "Kandy Temple of Tooth", "Sigiriya Rock Fortress", "Nuwara Eliya Tea Gardens", "Yala National Park Safari", "Galle Fort"],
    "philippines": ["Manila City Tour", "Boracay White Beach", "Palawan Underground River", "Cebu Whale Sharks", "Bohol Chocolate Hills", "El Nido Island Hopping"],
    "singapore": ["Gardens by the Bay", "Marina Bay Sands", "Sentosa Island", "Universal Studios", "Night Safari", "Merlion Park"],
    "malaysia": ["Kuala Lumpur Petronas Towers", "Batu Caves", "Langkawi Cable Car", "Penang George Town", "Genting Highlands", "Malacca Historic City"],
    "turkey": ["Istanbul Hagia Sophia", "Cappadocia Hot Air Balloon", "Pamukkale Thermal Pools", "Ephesus Ruins", "Antalya Coastal Tour", "Bosphorus Cruise"],
    "georgia": ["Tbilisi Old Town", "Kazbegi Mountains", "Mtskheta Ancient Capital", "Signagi City of Love", "Uplistsikhe Cave Town", "Batumi Black Sea Coast"],
    "bhutan": ["Paro Taktsang (Tiger's Nest)", "Thimphu Buddha Dordenma", "Punakha Dzong", "Dochula Pass", "Phobjikha Valley", "National Museum"]
}

generic_activities = ["Local City Tour", "Leisure & Shopping", "Cultural Experience", "Nature Walk", "Scenic Drive", "Rest Day"]

def generate_itinerary(dest_slug, duration_str):
    # Parse duration e.g., "5N/6D" -> 6 days
    try:
        days = int(duration_str.split('/')[1].replace('D', ''))
    except (IndexError, ValueError, AttributeError):
        days = 5
        
    activities = highlights.get(dest_slug, generic_activities)
    
    itinerary = []
    
    for i in range(1, days + 1):
        if i == 1:
            title = "Arrival & Check-in"
            desc = f"Arrive at the destination. Transfer to your pre-booked hotel. Spend the rest of the day relaxing and acclimating to the new surroundings."
            meta1 = "Airport Transfer"
            icon1 = "fa-plane-arrival"
        elif i == days:
            title = "Departure"
            desc = "Enjoy your final breakfast. Check out from the hotel and transfer to the airport for your onward journey with wonderful memories."
            meta1 = "Airport Transfer"
            icon1 = "fa-plane-departure"
        else:
            # Pick a unique activity if available, else pick random
            activity_idx = (i - 2) % len(activities)
            title = activities[activity_idx]
            desc = f"After a hearty breakfast, head out for {title}. Experience the local culture, take beautiful photos, and enjoy the guided tour."
            meta1 = "Sightseeing"
            icon1 = "fa-camera"
            
        day_obj = {
            "day": i,
            "title": title,
            "meta_1": meta1,
            "icon_1": icon1,
            "description": desc
        }
        itinerary.append(day_obj)
        
    return itinerary

# Read current destinations.json
with open('data/destinations.json', 'r') as f:
    dest_data = json.load(f)

for dest in dest_data:
    dest['itinerary'] = generate_itinerary(dest['slug'], dest['duration'])

# Save it back
with open('data/destinations.json', 'w') as f:
    json.dump(dest_data, f, indent=4)
    
print("Successfully injected unique itineraries into data/destinations.json")
