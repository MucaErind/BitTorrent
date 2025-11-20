import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "frontend"  # Cartella da servire

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se viene richiesto solo l'URL base, serve index.html
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Cambia la directory di lavoro corrente alla cartella dove si trova lo script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend Web Server attivo su http://localhost:{PORT}")
    print(f"Apri il browser su: http://localhost:{PORT}")
    httpd.serve_forever()