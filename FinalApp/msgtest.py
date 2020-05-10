import requests

def post():
    print("writing post request to port 8088")
    mydata = {'from_user':'test', 'to_user':'nikita', 'message':'hello there'}
    print(type(mydata))
    print(mydata)
    requests.post('http://127.0.0.1:8088', data = mydata)

def get():
    print("get request")
    mydata = {'user':'nikita'}
    print(mydata)
    #requests.get('http://127.0.0.1:8088?user=nikita', data = mydata)
    msgs = requests.get('http://127.0.0.1:8088', params=mydata)
    print(type(msgs))
    print(msgs.text)

get()
for i in range(100):
    #post()
    ...
