import os
import re

with open('templates/package-detail.html.j2', 'r') as f:
    html = f.read()

# Strip dynamic script if present
script_start = html.find('// Dynamic Mockup Script')
if script_start != -1:
    script_end = html.find('</script>', script_start)
    if script_end != -1:
        html = html[:script_start] + html[script_end:]

html = html.replace('Mauritius', '{{ dest.name }}')
html = html.replace('9N/10D', '{{ dest.duration }}')
html = html.replace('99,625', '{{ dest.price }}')
html = html.replace('9 Nights 10 Days', '{{ nights }} Nights {{ days }} Days')
html = html.replace('https://kanholidays.com/storage/packages/UlyvqXb5RyM78ywNx8t4CqSdvQUKE99LYKf9nxzt.png', '{{ dest.hero_image }}')

# Replace the ITINERARY_HTML placeholder with proper Jinja loop
itinerary_template = """{% for day in dest.itinerary %}
            <div class="itinerary-day{% if loop.index0 == 0 %} active{% endif %}">
              <div class="itinerary-day__marker"><div class="itinerary-day__marker-dot"></div></div>
              <div class="itinerary-day__header" onclick="toggleDay(this)">
                <span class="itinerary-day__number">Day {{ day.day }}</span>
                <span class="itinerary-day__title">{{ day.title }}</span>
                <i class="fas fa-chevron-down itinerary-day__toggle"></i>
              </div>
              <div class="itinerary-day__body">
                <div class="itinerary-day__content">
                  <div class="itinerary-day__meta">
                    <span class="itinerary-meta-item"><i class="fas {{ day.icon_1 }}"></i> {{ day.meta_1 }}</span>
                    <span class="itinerary-meta-item"><i class="fas fa-utensils"></i> Breakfast</span>
                  </div>
                  <p class="itinerary-day__text">{{ day.description }}</p>
                </div>
              </div>
            </div>
{% endfor %}"""

html = html.replace('{{ ITINERARY_HTML }}', itinerary_template)

highlights_template = """{% for hl in dest.highlights %}
<li style="display:flex;align-items:center;gap:var(--space-sm);font-size:var(--text-sm)"><i class="fas fa-check-circle" style="color:var(--color-success)"></i> {{ hl }}</li>
{% endfor %}"""

html = html.replace('{{ HIGHLIGHTS_HTML }}', highlights_template)
html = html.replace('{{ BEST_TIME }}', "{{ dest.best_time | default('Varies by season') }}")

with open('templates/package-detail.html.j2', 'w') as f:
    f.write(html)
