import datetime
import json
import requests
import pprint

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# Write a CustomDecoder

# get all contacts from the server
response = requests.get("http://127.0.0.1:5000/api/contacts/all")
contacts = json.loads(response.text, cls=CustomDecoder)
pprint.pprint(contacts)