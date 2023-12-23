
import socketserver
import http.server #SimpleHTTPServer
from  utillc import *
import urllib.request


PORT = 9097
class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url=self.path[1:]
        self.send_response(200)
        self.end_headers()
        r = urllib.request.urlopen(url)
        self.copyfile(r, self.wfile)

httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print ("Now serving at %d" % PORT)
httpd.serve_forever()

