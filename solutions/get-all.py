import datetime
import json
import requests
import pprint

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.decode_contact, *args, **kwargs)
    
    def decode_contact(self, data):
        if "last_contact" in data:
            data["last_contact"] = datetime.date.fromisoformat(data["last_contact"])

        return data

# get all contacts from the server
response = requests.get("http://127.0.0.1:5000/api/contacts/all")
contacts = json.loads(response.text, cls=CustomDecoder)
pprint.pprint(contacts)