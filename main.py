import sys
import socketserver
from http.server import SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", 8081), SimpleHTTPRequestHandler)

print("Serving at port 8081")
httpd.serve_forever()


