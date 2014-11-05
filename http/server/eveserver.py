import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.1"

class TestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
       self.send_response(200)
       self.send_header('Content-Type', 'application/json')
       self.end_headers()

       self.wfile.write("<?xml version='1.0'?>");
       self.wfile.write("<sample>Some XML</sample>");
       self.wfile.close();

port = 5000
server_address = ("0.0.0.0",port)

httpd = ServerClass(server_address,TestHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()