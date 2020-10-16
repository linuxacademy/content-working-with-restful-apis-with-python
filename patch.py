import datetime
import json
import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# correct the misspelling of carrots on contact-id #1
data = {
    "favorite_food": "carrots",
    "last_contact": datetime.date.today()
}

# write CustomEncoder

response = requests.patch("http://127.0.0.1:5000/api/contacts/1", json=json.dumps(data, cls=CustomEncoder))
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)
