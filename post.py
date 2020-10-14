import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# create a new contact name Tweety, favorite foods seeds
data = {
    "name": "Tweety",
    "address": None,
    "favorite_food": "seeds",
    "last_contact": "2020-10-31"
}

response =
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)