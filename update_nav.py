import os
import re

# Extract nav from index.html
with open('index.html', 'r') as f:
    index_content = f.read()

nav_match = re.search(r'<nav class="main-nav" id="mainNav">.*?</nav>', index_content, re.DOTALL)
if not nav_match:
    print("Could not find nav in index.html")
    exit(1)
    
new_nav = nav_match.group(0)

# Also extract the mobile menu
mobile_match = re.search(r'<div class="mobile-menu" id="mobileMenu">.*?</div>', index_content, re.DOTALL)
new_mobile = mobile_match.group(0) if mobile_match else ""

files_to_update = [
    'templates/package-detail.tpl.html',
    'about-us.html',
    'blogs.html',
    'corporate.html',
    'destinations.html',
    'experiences.html',
    'pay-us.html',
    'upcoming-trips.html',
    'visa.html'
]

for filename in files_to_update:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Replace nav
    content = re.sub(r'<nav class="main-nav" id="mainNav">.*?</nav>', new_nav, content, flags=re.DOTALL)
    
    # Replace mobile menu if exists
    if new_mobile:
        content = re.sub(r'<div class="mobile-menu" id="mobileMenu">.*?</div>', new_mobile, content, flags=re.DOTALL)
        
    with open(filename, 'w') as f:
        f.write(content)
        
print("Updated nav in all files")
