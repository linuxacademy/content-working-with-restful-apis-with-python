import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# create "response" request for all 
response = requests.get("http://127.0.0.1:5000/api/contacts/all")

#  For Office Use Only, Please Do Not Change Code Below
expected = """{
  "data": [
    {
      "address": "1 Carrot Lane, Toontown", 
      "contact_id": "1", 
      "favorite_food": "carots", 
      "name": "Bugs Bunny"
    }, 
    {
      "address": "5 Alleyway, Toontown", 
      "contact_id": "2", 
      "favorite_food": "Tweety", 
      "name": "Sylvester"
    }, 
    {
      "address": "32 Dog Lake, Toontowm", 
      "contact_id": "3", 
      "favorite_food": "Scooby Snacks", 
      "name": "Scooby Doo"
    }
  ]
}
"""


try:
    assert response == expected
except AssertionError:
    print("Expected: ", expected)
    print("Response: ", response.text)
    print("They do not match.")
else:
    print("\n\Congratulations Cloud Guru! You completed the lab.\n\n")