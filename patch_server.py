import re
# Testing logic for mapping package to destination
req_path = "/packages/bali-honeymoon-bliss"
if req_path.startswith('/packages/'):
    slug = req_path.split('/')[-1]
    # Simple keyword match
    destinations = ["bali", "dubai", "maldives", "kashmir", "mauritius", "europe", "greece", "switzerland", "russia", "ladakh", "himachal-pradesh", "uttarakhand", "spiti", "rajasthan", "meghalaya", "sikkim", "andaman", "kerala", "goa", "coorg", "arunachal-pradesh", "varanasi", "odisha", "vietnam", "thailand", "japan", "sri-lanka", "philippines", "singapore", "malaysia", "turkey", "georgia", "bhutan"]
    matched = "mauritius" # default
    for d in destinations:
        if d in slug:
            matched = d
            break
    print(f"/destinations/{matched}.html")
