import requests

print("writing post request to port 8088")
mydata = {'from_user':'test', 'to_user':'nikita', 'message':'hello there'}
print(type(mydata))
print(mydata)
requests.post('http://127.0.0.1:8088', data = mydata)


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
