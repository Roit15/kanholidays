import http.server
import socketserver
import os

PORT = 3000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract the path without query strings for file checking
        req_path = self.path.split('?')[0]
        file_path = self.translate_path(req_path)
        
        if not os.path.exists(file_path):
            # Try appending .html to the path
            if os.path.exists(file_path + '.html'):
                self.path = req_path + '.html' + ('?' + self.path.split('?')[1] if '?' in self.path else '')
            # Try appending /index.html to the path
            elif os.path.exists(os.path.join(file_path, 'index.html')):
                self.path = req_path + '/index.html' + ('?' + self.path.split('?')[1] if '?' in self.path else '')
            # If it's a dynamic destination route, it will just find the file because we generate them as /destinations/slug.html
            # Map specific packages to their destination equivalent
            elif req_path.startswith('/packages/'):
                slug = req_path.split('/')[-1]
                destinations = ["bali", "dubai", "maldives", "kashmir", "mauritius", "europe", "greece", "switzerland", "russia", "ladakh", "himachal-pradesh", "uttarakhand", "spiti", "rajasthan", "meghalaya", "sikkim", "andaman", "kerala", "goa", "coorg", "arunachal-pradesh", "varanasi", "odisha", "vietnam", "thailand", "japan", "sri-lanka", "philippines", "singapore", "malaysia", "turkey", "georgia", "bhutan"]
                matched = "mauritius" # default fallback
                for d in destinations:
                    if d in slug:
                        matched = d
                        break
                self.path = f'/destinations/{matched}.html'
            # If it's /honeymoon, map to experiences or destinations
            elif req_path == '/honeymoon':
                self.path = '/experiences.html'
            # If it's /destinations (directory), map to destinations.html
            elif req_path.rstrip('/') == '/destinations':
                self.path = '/destinations.html'
            # If it's /about, map to about-us
            elif req_path == '/about':
                self.path = '/about-us.html'
            # If it's /pay-us
            elif req_path == '/pay-us':
                self.path = '/pay-us.html'

        return super().do_GET()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT} with clean URL support...")
    httpd.serve_forever()
