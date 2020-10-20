import datetime
import json
import requests

from flask_server import Contact

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# correct the misspelling of carrots on contact-id #1
data = {
    "favorite_food": "carrots",
    "last_contact": datetime.date.today()
}
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, Contact):
            return obj.__dict__
        elif obj.__class__.__name__ == "dict_values":
            return list(obj)
        
        return super().default(obj)

json_data = json.dumps(data, cls=CustomEncoder)
print(json_data)
response = requests.patch("http://127.0.0.1:5000/api/contacts/1", data=json.dumps(data, cls=CustomEncoder))
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)
