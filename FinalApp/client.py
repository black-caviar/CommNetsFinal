import requests

print("writing post request to port 8088")
mydata = {'from_user':'test', 'to_user':'nikita', 'message':'hello there'}
print(type(mydata))
print(mydata)
requests.post('http://127.0.0.1:8088', data = mydata)
