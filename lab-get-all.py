import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

response = requests.get("http://127.0.0.1:5000/api/contacts/all")

print(response.text)