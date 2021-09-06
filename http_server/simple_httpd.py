import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()


# curl localhost:8000/hello_world.txt will return the file, since
# it serves files relative to the current directory
