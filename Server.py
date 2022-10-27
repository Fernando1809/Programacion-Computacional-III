from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 2402

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.path = "FashonNae.html"
        return SimpleHTTPRequestHandler.do_GET(self)

print("Servidor corriendo en el pueto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()