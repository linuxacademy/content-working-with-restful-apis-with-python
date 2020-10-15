import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# create a new contact name Tweety, favorite foods seeds


response =
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)