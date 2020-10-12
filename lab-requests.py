import requests

URL = "http://127.0.0.1:5000"

def get():
    return requests.get("http://127.0.0.1:5000/")

def post():
    data = {
        "name": "Tweety",
        "address": None,
        "fav-food": "seeds"
    }

    requests.post("http://127.0.0.1:5000/", json=data)

def put():
    data = {
        "id": 3,
        "name": "Tweety Bird",
        "address": "1 Bird Cage, Queensland, AUS",
        "fav-food": "seeds, nuts, bits"
    }

    requests.put("http://127.0.0.1:5000/", json=data)

def patch():
    data = {
        "id": 1,
        "fav-food": "carrots"
    }
    requests.patch("http://127.0.0.1:5000/", json=data)

def delete():
    data = {
        "id": 4
    }
    requests.delete("http://127.0.0.1:5000/", json=data)

if __name__ == "__main__":
    delete()
    print(get().text)