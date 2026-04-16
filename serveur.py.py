from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

DATA_FILE = "data.json"

# créer fichier si absent
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/load":
            with open(DATA_FILE, "r") as f:
                data = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data.encode())

    def do_POST(self):
        if self.path == "/save":
            length = int(self.headers.get('Content-Length'))
            body = self.rfile.read(length)

            with open(DATA_FILE, "wb") as f:
                f.write(body)

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

server = HTTPServer(("localhost", 8000), Handler)
print("Serveur lancé sur http://localhost:8000")
server.serve_forever()