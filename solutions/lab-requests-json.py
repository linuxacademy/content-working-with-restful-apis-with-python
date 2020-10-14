import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"


def get():
    return requests.get("http://127.0.0.1:5000/api/contacts/all")

def get_one(contact_id):
    return requests.get("http://127.0.0.1:5000/api/contacts/%s" % contact_id)

# right a post requests using json for the endpt "/"
def post():
    data = {
        "name": "Tweety",
        "address": None,
        "favorite_food": "seeds",
        "last_contact": "2019-08-04"
    }

    return requests.post("http://127.0.0.1:5000/api/contacts/new", json=data)

# right a put requests to replace id # 3 using json for the endpt "/"
def put(contact_id):
    data = {
        "contact_id": "4",
        "name": "Tweety Bird",
        "address": "1 Bird Cage, Queensland, AUS",
        "favorite_food": "seeds, nuts, bits",
        "last_contact": "2020-08-10"
    }

    return requests.put("http://127.0.0.1:5000/api/contacts/%s" % contact_id, json=data)
    

# right a patch requests to update entry #1 using json for the endpt "/"
def patch():
    data = {
        "favorite_food": "carrots"
    }
    return requests.patch("http://127.0.0.1:5000/api/contacts/1", json=data)

# right a delete requests to replace id #4 using json for the endpt "/"
def delete(contact_id):

    return requests.delete("http://127.0.0.1:5000/api/contacts/" + str(contact_id))

if __name__ == "__main__":
    response = put(4)
    print("\n------------\n")
    print("Headers: ", response.headers)
    print("\n------------\n")
    print("Status Code: ", response.status_code)
    print("\n------------\n")
    print("Results: ", response.text)
    print("\n------------")
    