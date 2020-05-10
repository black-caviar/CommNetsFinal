#username = input("Username: ")
#print("Welcome", username)
# do fetch messages
#while True:
    #line = input(':')
    # parse line for @ signs, store them to list
    # parse for 'q' or 'r' to signify refresh or quit

#import read
import re
import requests
import json
    
HOST = '127.0.0.1'
PORT = 8088
    
def get_messages(username, sent_after):
    data = {'user':username, 'time':sent_after}
    msgs = requests.get('http://{}:{}'.format(HOST,PORT), params=data)
    print(type(msgs.json()))

def send_message(msg):
    dest_user = re.findall('@\S*',msg)
    print(dest_user)
    data = {}
    data['from_user'] = USERNAME
    data['message'] = msg
    for i in dest_user:
        data['to_user'] = i
        requests.post('http://{}:{}'.format(HOST,PORT), data=data)
    

USERNAME = input('Username? ')
print("Welcome", USERNAME)
get_messages(USERNAME, 0)


while True:
    msg = input(": ")
    send_message(msg)

    
# step 1: ask for username
# step 2: fetch messages from server
# step 3: enter user interaction loop
#         periodically check for new messages for user
#         provide user with command line environment
#         for typing text messages
#         provide some keywords such as refresh or quit
#
#
#
# Sample User Interaction
#
#
# From Nikita
# Hello there this is a sample incoming message
#
#
# From Marc
# Haha
#
#                                          @Marc @Nikita this is a great app
#
#
# It would be ideal if you could @username people 
