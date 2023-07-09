import sys
import requests

# this if condition ensures that the code block below it is executed only when the script is run directly and not when the script is imported as a module
if __name__ == "__main__":
    # retrieves the first command-line argument passed to the script and converts it to lowercase.
    order = sys.argv[1].lower()

    user = None
    users = None
    #GET REQUEST TO retrieve a specific user's information with ID 1
    if order == "get_json":
        resp = requests.get("http://localhost:5000/api/users/1")
        user = resp.json()
    #GET REQUEST TO retrieve a list of all of the users in either a database or in a python list possibly
    elif order == "list_json":
        resp = requests.get("http://localhost:5000/api/users")
        users = resp.json()
    #POST request to create a new user with the specified json payload in the body list 
    elif order == "create_json":
        body = {
            "name": "Lance Armstrong",
            "occupation": "Cyclist",
            "birthday": "2000-01-01",
        }
        resp = requests.post("http://localhost:5000/api/users/new", json=body)
        user = resp.json()
    #PUT request to update an existing user id with ID 1 using the specified json payload in the body lisst
    elif order == "update_json":
        body = {
            "name": "Bob Barker",
            "occupation": "TV Show Host",
            "birthday": "1923-12-12",
        }
        resp = requests.put("http://localhost:5000/api/users/1", json=body)
        user = resp.json()
    #DELETE a user from either the database or python list with the ID of 1
    elif order == "delete_json":
        resp = requests.delete("http://localhost:5000/api/users/1")
        user = resp.json()
    else: #order variable does not match predefined options aka invalid command was provided as command line argument
        print("Invalid command")
        #script exists with a non zero status code, indicating an error condition as the script terminated abnormally due to an invalid command being provided by the user 
        sys.exit(1)

    print(resp.status_code)
    print(resp.text)

    if user:
        print(user)

    if users:
        print(users)
