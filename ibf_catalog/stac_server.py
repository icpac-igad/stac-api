# Python 3 STAC server with CORS headers
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import os

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
print(f"Starting STAC server on port {port}...")
print(f"Access your FloodWatch STAC catalog at:")
print(f"  Direct: http://localhost:{port}/flood/fl_catalog.json")
print(f"  STAC Browser: https://radiantearth.github.io/stac-browser/#/external/http://localhost:{port}/flood/fl_catalog.json")
print(f"\nPress Ctrl+C to stop the server")

try:
    HTTPServer(('', port), CORSRequestHandler).serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
