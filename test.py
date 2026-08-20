import re

with open('css/package-detail.css', 'r') as f:
    css = f.read()

# Add .pkg-content { min-width: 0; } if not exists
if '.pkg-content' not in css:
    css = css.replace('.pkg-layout {\n  display: grid;', '.pkg-content { min-width: 0; overflow: hidden; }\n\n.pkg-layout {\n  display: grid;')
    
with open('css/package-detail.css', 'w') as f:
    f.write(css)
print("Done")
