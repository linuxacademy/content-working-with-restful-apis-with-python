import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# get all contacts from the server
response = 
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)