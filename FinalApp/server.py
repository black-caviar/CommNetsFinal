from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import cgi
import sqlite3
import atexit
import json

PORT = 8088


def load_db(db):
    try:
        db.execute("SELECT from_user, to_user, date, message FROM messages")
        print("Database loaded successfully")
    except sqlite3.OperationalError as e:
        print("Operational error in SQL")
        print(str(e))
        if input("Create new DB? yes/no ") == 'yes':
            db.execute('''CREATE TABLE messages (from_user text, to_user text, date text, message text)''')
        else:
            print("DB unmodified")
            exit()

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
        #print(parse_qs(self.path[2:]))
        get_opt = parse_qs(self.path[2:])
        print(get_opt)
        print(get_opt['user'])
        users = get_opt['user']
        msg_dict = {}
        for i in users:
            print(i)
            c.execute("SELECT from_user, date, message FROM messages WHERE to_user = '%s'" % i)
            response = c.fetchall()
            #try getting all messages sent after a certain time
            #print(type(response))
            #print(type(response[1]))
            msg_dict[i] = response
            #data_str = json.dumps(response)
            #print(data_str)
        #self.wfile.write(str.encode("<html><body><h1>Get Request Received!</h1></body></html>"))
        json_str = json.dumps(msg_dict)
        self.wfile.write(str.encode(json_str))
       
        
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        vals = [form.getvalue("from_user"), form.getvalue("to_user"), 'now',  form.getvalue("message")]
        print(vals)
        c.execute('''INSERT INTO messages VALUES (?,?,?,?)''', vals)
        c.commit()
        self.wfile.write(str.encode("<html><body><h1>POST Request Received!</h1></body></html>"))
        # is this even necessary?
        # This is a response to the post request. Maybe write like success?
        # Then we can have a message received or failed status code

def run(server_class=HTTPServer, handler_class=GP, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:8088...')
    httpd.serve_forever()

db = sqlite3.connect('messages.db')
atexit.register(db.close)
c = db.cursor()
load_db(c)
run()
