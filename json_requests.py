import sys
import requests

if __name__ == "__main__":
    order = sys.argv[1].lower()

    user = None
    users = None

    if order == "get_json":
        resp = requests.get("http://localhost:5000/api/users/1")
        user = resp.json()
    elif order == "list_json":
        resp = requests.get("http://localhost:5000/api/users")
        users = resp.json()
    elif order == "create_json":
        body = {
            "name": "Lance Armstrong",
            "occupation": "Cyclist",
            "birthday": "2000-01-01",
        }
        resp = requests.post("http://localhost:5000/api/users/new", json=body)
        user = resp.json()
    elif order == "update_json":
        body = {
            "name": "Bob Barker",
            "occupation": "TV Show Host",
            "birthday": "1923-12-12",
        }
        resp = requests.put("http://localhost:5000/api/users/1", json=body)
        user = resp.json()
    elif order == "delete_json":
        resp = requests.delete("http://localhost:5000/api/users/1")
        user = resp.json()
    else:
        print("Invalid command")
        sys.exit(1)

    print(resp.status_code)
    print(resp.text)

    if user:
        print(user)

    if users:
        print(users)
