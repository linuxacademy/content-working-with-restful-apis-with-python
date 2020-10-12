import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# right a get request for the endpt "/"
def get():
    return 

# right a post requests using json for the endpt "/"
def post():
    data = {
        "name": "Tweety",
        "address": None,
        "fav-food": "seeds"
    }

    return 

# right a put requests to replace id # 3 using json for the endpt "/"
def put():
    data = {
        "id": 3,
        "name": "Tweety Bird",
        "address": "1 Bird Cage, Queensland, AUS",
        "fav-food": "seeds, nuts, bits"
    }

    return 
    

# right a patch requests to update entry #1 using json for the endpt "/"
def patch():
    data = {
        "id": 1,
        "fav-food": "carrots"
    }
    return 

# right a delete requests to replace id #4 using json for the endpt "/"
def delete():
    data = {
        "id": 4
    }

    return 

if __name__ == "__main__":
    # change the method to the one you want, ie., get(), post(), etc.
    response = 
    print("\n------------\n")
    print("Headers: ", response.headers)
    print("\n------------\n")
    print("Status Code: ", response.status_code)
    print("\n------------\n")
    print("Results: ", response.text)
    print("\n------------")
    