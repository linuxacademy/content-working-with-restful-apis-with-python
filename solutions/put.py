import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# update tweety
data = {
    "id": "4",
    "name": "Tweety Bird",
    "address": "1 Bird Cage, Queensland, AUS",
    "favorite_food": "seeds, nuts, bits"
}

response = requests.put("http://127.0.0.1:5000/api/contacts/4", json=data)
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)