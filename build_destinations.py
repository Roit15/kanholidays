import json
import os
from jinja2 import Environment, FileSystemLoader

# Load destinations data
with open('data/destinations.json', 'r') as f:
    destinations = json.load(f)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('package-detail.html.j2')

# Ensure output directory exists
os.makedirs('destinations', exist_ok=True)

for dest in destinations:
    try:
        nights, days = dest.get('duration', '0N/0D').split('/')
        n_num = nights.replace('N', '')
        d_num = days.replace('D', '')
    except:
        n_num, d_num = "0", "0"

    html_content = template.render(
        dest=dest,
        nights=n_num,
        days=d_num
    )
    
    out_path = f"destinations/{dest['slug']}.html"
    with open(out_path, 'w') as f:
        f.write(html_content)
        
print(f"Successfully generated {len(destinations)} destination pages using Jinja2!")
