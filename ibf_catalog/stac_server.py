# Python 3 server with CORS headers
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        # Handle OPTIONS requests for CORS preflight
        self.send_response(200)
        self.end_headers()

# Set port (default 8000)
port = 8000
if len(sys.argv) > 1:
    port = int(sys.argv[1])

# Start server
print(f"Starting server on port {port}...")
print(f"Access your STAC catalog at: http://localhost:{port}/catalog.json")
HTTPServer(('', port), CORSRequestHandler).serve_forever()
