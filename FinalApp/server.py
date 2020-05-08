from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import cgi
import sqlite3

conn = sqlite3.connect('messages.db')
# This needs error check
c = conn.cursor()
#check if table already exists, otherwise create it
#c.execute('''CREATE TABLE messages (from_user text, to_user text, date text, message text)''')


class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print(self.path)
        print(parse_qs(self.path[2:]))
        self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        print(form.getvalue("from_user"))
        print(form.getvalue("to_user"))
        print(form.getvalue("message"))
        vals = [form.getvalue("from_user"), form.getvalue("to_user"), 'now',  form.getvalue("message")]
        print(vals)
        c.execute('''INSERT INTO messages VALUES (?,?,?,?)''', vals)
        conn.commit()
        self.wfile.write(str.encode("<html><body><h1>POST Request Received!</h1></body></html>"))

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:8088...')
    httpd.serve_forever()

run()
