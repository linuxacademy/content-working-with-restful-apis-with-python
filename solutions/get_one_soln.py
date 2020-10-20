import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# get contact_id #1 from the server
response = requests.get("http://127.0.0.1:5000/api/contacts/1")
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)