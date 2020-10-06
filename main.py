import sys
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

class AWServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Ohai world!", "utf-8"))
        

aw_server = HTTPServer(("", 8081), AWServer)

try:
    aw_server.serve_forever()
except:
    pass

aw_server.server_close()



