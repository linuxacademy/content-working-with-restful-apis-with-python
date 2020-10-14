import sys
import requests

import json
from users_api import User, UserDecoder, CustomEncoder

if __name__ == "__main__":
    order = sys.argv[1].lower()

    user = None
    users = None

    if order == "get_json":
        resp = requests.get("http://localhost:5000/api/users/1")
        user = resp.json(cls=UserDecoder)
    elif order == "list_json":
        resp = requests.get("http://localhost:5000/api/users")
        users = resp.json(cls=UserDecoder)
    elif order == "create_json":
        body = User(
            None,
            {
                "name": "Lance Armstrong",
                "occupation": "Cyclist",
                "birthday": "2000-01-01",
            },
        )
        resp = requests.post(
            "http://localhost:5000/api/users/new",
            data=json.dumps(body, cls=CustomEncoder),
            headers={"Content-Type": "application/json"},
        )
        user = resp.json(cls=UserDecoder)
    elif order == "update_json":
        body = User(
            1,
            **{
                "name": "Bob Barker",
                "occupation": "TV Show Host",
                "birthday": "1923-12-12",
            }
        )
        resp = requests.put(
            "http://localhost:5000/api/users/1",
            data=json.dumps(body, cls=CustomEncoder),
            headers={"Content-Type": "application/json"},
        )
        user = resp.json(cls=UserDecoder)
    elif order == "delete_json":
        resp = requests.delete("http://localhost:5000/api/users/1")
        user = resp.json(cls=UserDecoder)
    else:
        print("Invalid command")
        sys.exit(1)

    print(resp.status_code)
    print(resp.text)

    if user:
        print(user.__dict__)

    if users:
        print(users)
