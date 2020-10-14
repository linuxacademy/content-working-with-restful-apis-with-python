import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# change the Tweety contact
data = {
    "contact_id": "4",
    "name": "Tweety Bird",
    "address": "1 Bird Cage, Queensland, AUS",
    "favorite_food": "seeds, nuts, bits"
}

response =
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)