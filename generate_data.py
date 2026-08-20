import json

destinations_list = [
    "bali", "dubai", "maldives", "kashmir", "mauritius", "europe", "greece", 
    "switzerland", "russia", "ladakh", "himachal-pradesh", "uttarakhand", "spiti", 
    "rajasthan", "meghalaya", "sikkim", "andaman", "kerala", "goa", "coorg", 
    "arunachal-pradesh", "varanasi", "odisha", "vietnam", "thailand", "japan", 
    "sri-lanka", "philippines", "singapore", "malaysia", "turkey", "georgia", "bhutan"
]

images = {
    "bali": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=1600&q=80",
    "dubai": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=1600&q=80",
    "maldives": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=1600&q=80",
    "kashmir": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=1600&q=80",
    "mauritius": "https://images.unsplash.com/photo-1540202404-1b927e27fa8b?w=1600&q=80",
    "europe": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1600&q=80",
    "greece": "https://images.unsplash.com/photo-1533105079780-92b9be482077?w=1600&q=80",
    "switzerland": "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=1600&q=80",
    "japan": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1600&q=80",
    "default": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=1600&q=80"
}

data = []
for slug in destinations_list:
    name = " ".join([word.capitalize() for word in slug.split('-')])
    
    # Generic realistic pricing (mock logic)
    if slug in ["europe", "switzerland", "usa", "japan"]:
        price = "1,45,000"
        duration = "8N/9D"
    elif slug in ["dubai", "bali", "vietnam", "thailand", "malaysia", "singapore", "sri-lanka"]:
        price = "45,500"
        duration = "5N/6D"
    elif slug in ["maldives", "mauritius"]:
        price = "89,999"
        duration = "4N/5D"
    else: # Domestic
        price = "25,000"
        duration = "6N/7D"

    item = {
        "slug": slug,
        "name": name,
        "hero_image": images.get(slug, images["default"]),
        "price": price,
        "duration": duration,
        "description": f"The Complete {name} Experience — {duration} tour package from ₹{price} per person."
    }
    data.append(item)

with open('data/destinations.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Generated data/destinations.json")
