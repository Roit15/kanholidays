import json
import os
import re

# Load destinations data
with open('data/destinations.json', 'r') as f:
    destinations = json.load(f)

# Load template
with open('templates/package-detail.tpl.html', 'r') as f:
    template = f.read()

# Strip out the dynamic JS mockup script that was at the bottom
script_start = template.find('// Dynamic Mockup Script')
if script_start != -1:
    script_end = template.find('</script>', script_start)
    if script_end != -1:
        template = template[:script_start] + template[script_end:]

# Ensure output directory exists
os.makedirs('destinations', exist_ok=True)

for dest in destinations:
    html = template
    
    # Text replacements
    html = html.replace('Mauritius', dest['name'])
    html = html.replace('9N/10D', dest['duration'])
    html = html.replace('99,625', dest['price'])
    
    # Generate Highlights HTML
    highlights_html = ""
    for hl in dest.get('highlights', []):
        highlights_html += f'<li style="display:flex;align-items:center;gap:var(--space-sm);font-size:var(--text-sm)"><i class="fas fa-check-circle" style="color:var(--color-success)"></i> {hl}</li>\n'
    html = html.replace('{{ HIGHLIGHTS_HTML }}', highlights_html)
    
    # Replace Best Time
    html = html.replace('{{ BEST_TIME }}', dest.get('best_time', 'Varies by season'))
    
    # Generate Itinerary HTML
    itinerary_html = ""
    for idx, day in enumerate(dest.get('itinerary', [])):
        active_class = " active" if idx == 0 else ""
        itinerary_html += f"""
            <div class="itinerary-day{active_class}">
              <div class="itinerary-day__marker"><div class="itinerary-day__marker-dot"></div></div>
              <div class="itinerary-day__header" onclick="toggleDay(this)">
                <span class="itinerary-day__number">Day {day['day']}</span>
                <span class="itinerary-day__title">{day['title']}</span>
                <i class="fas fa-chevron-down itinerary-day__toggle"></i>
              </div>
              <div class="itinerary-day__body">
                <div class="itinerary-day__content">
                  <div class="itinerary-day__meta">
                    <span class="itinerary-meta-item"><i class="fas {day['icon_1']}"></i> {day['meta_1']}</span>
                    <span class="itinerary-meta-item"><i class="fas fa-utensils"></i> Breakfast</span>
                  </div>
                  <p class="itinerary-day__text">{day['description']}</p>
                </div>
              </div>
            </div>
"""
    html = html.replace('{{ ITINERARY_HTML }}', itinerary_html)

    
    # Also replace 9 Nights 10 Days in meta description if necessary
    # Example parsing from "9N/10D" to "9 Nights 10 Days"
    try:
        nights, days = dest['duration'].split('/')
        n_num = nights.replace('N', '')
        d_num = days.replace('D', '')
        html = html.replace('9 Nights 10 Days', f"{n_num} Nights {d_num} Days")
    except:
        pass
        
    # Replace Hero Image
    # Current image in template is: https://kanholidays.com/storage/packages/UlyvqXb5RyM78ywNx8t4CqSdvQUKE99LYKf9nxzt.png
    html = html.replace(
        'https://kanholidays.com/storage/packages/UlyvqXb5RyM78ywNx8t4CqSdvQUKE99LYKf9nxzt.png', 
        dest['hero_image']
    )
    
    # Save the file
    out_path = f"destinations/{dest['slug']}.html"
    with open(out_path, 'w') as f:
        f.write(html)
        
print(f"Successfully generated {len(destinations)} destination pages!")
