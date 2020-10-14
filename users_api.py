try:
    from flask import Flask, request, jsonify

    import defusedxml.ElementTree as ET
except:
    import sys

    print("\nPlease install dependencies via\n\npython -m pip install Flask defusedxml")
    sys.exit(1)

import datetime
from xml.etree.ElementTree import Element, SubElement
from xml.dom.minidom import parseString

app = Flask(__name__)

from json import JSONDecoder, JSONEncoder


class User:
    def __init__(self, user_id, name, occupation, birthday):
        self.user_id = user_id
        self.name = name
        self.occupation = occupation
        self.birthday = birthday

    def update(self, name=None, occupation=None, birthday=None, *args, **kwargs):
        if name:
            self.name = name

        if occupation:
            self.occupation = occupation

        if birthday:
            self.birthday = birthday

    def to_xml(self):
        element = Element("user")
        element.set("id", str(self.user_id))

        name_tag = SubElement(element, "name")
        name_tag.text = str(self.name)

        occupation_tag = SubElement(element, "occupation")
        occupation_tag.text = str(self.occupation)

        birthday_tag = SubElement(element, "birthday")
        birthday_tag.text = self.birthday.isoformat()

        return element


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, User):
            return obj.__dict__
        elif obj.__class__.__name__ == "dict_values":
            return list(obj)

        return super().default(obj)


class UserDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.decode_user, *args, **kwargs)

    def decode_user(self, json_object):
        if "id" in json_object:
            json_object["user_id"] = json_object["id"]
            del json_object["id"]
        else:
            next_id = int(sorted(USERS.keys())[-1]) + 1
            json_object["user_id"] = next_id

        if "birthday" in json_object:
            json_object["birthday"] = datetime.date.fromisoformat(
                json_object["birthday"]
            )

        return User(**json_object)


app.json_encoder = CustomEncoder
app.json_decoder = UserDecoder

USERS = {
    1: User(1, "Keith Thompson", "Training Architect", datetime.date(1990, 1, 1)),
    2: User(2, "Kevin Bacon", "Actor", datetime.date(1958, 7, 8)),
    3: User(3, "Jason Fried", "Business Owner", datetime.date(1974, 4, 7)),
}


def find_user(user_id):
    return USERS.get(int(user_id))


def create_user(user_information: dict):
    next_id = int(sorted(USERS.keys())[-1]) + 1
    user = User(**user_information)
    user.user_id = next_id
    USERS[next_id] = user
    return user


def update_user(user_id, user_information: dict):
    user = find_user(user_id)
    if user:
        user.update(**user_information)

    return user


def delete_user(user_id):
    user = find_user(user_id)
    if user:
        del USERS[user.user_id]

    return user


# XML API


def parse_user_xml(xml_body):
    user_xml = ET.fromstring(xml_body)
    return {
        "user_id": user_xml.get("id"),
        "name": user_xml.findtext("name"),
        "occupation": user_xml.findtext("occupation"),
        "birthday": datetime.date.fromisoformat(user_xml.findtext("birthday")),
    }


def pretty_xml(root):
    xml_string = ET.tostring(root)
    dom = parseString(xml_string)
    return dom.toprettyxml(encoding="UTF-8")


@app.route("/api/xml/users", methods=["GET"])
def xml_user_index():
    root = Element("users")

    for u in USERS.values():
        root.append(u.to_xml())

    return pretty_xml(root), 200


@app.route("/api/xml/users/new", methods=["POST"])
def xml_user_new():
    user_information = parse_user_xml(request.data)
    user = create_user(user_information)
    return pretty_xml(user.to_xml()), 201


@app.route("/api/xml/users/<user_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def xml_user(user_id):
    if request.method == "GET":
        user = find_user(user_id)
        if user:
            return pretty_xml(user.to_xml()), 200
        else:
            return "Not found", 404
    elif request.method in ["PUT", "PATCH"]:
        user = find_user(user_id)
        if user:
            user.update(**parse_user_xml(request.data))
            return pretty_xml(user.to_xml()), 200
        else:
            return "Not found", 404
    else:
        user = delete_user(user_id)
        if user:
            return pretty_xml(user.to_xml()), 200
        else:
            return "Not found", 404


# JSON API


@app.route("/api/users", methods=["GET"])
def json_user_index():
    return jsonify(USERS.values()), 200


@app.route("/api/users/new", methods=["POST"])
def json_user_new():
    user = request.json  # Parses JSON to User and sets `user_id` to the next integer ID
    USERS[user.user_id] = user
    return jsonify(user), 201


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def json_user(user_id):
    if request.method == "GET":
        user = find_user(user_id)
        if user:
            return jsonify(user), 200
        else:
            return "Not found", 404
    elif request.method in ["PUT", "PATCH"]:
        user = find_user(user_id)
        new_user = request.json
        new_user.user_id = user_id
        if user:
            user.update(**new_user.__dict__)
            return jsonify(user), 200
        else:
            return "Not found", 404
    else:
        user = delete_user(user_id)
        if user:
            return jsonify(user), 200
        else:
            return "Not found", 404


if __name__ == "__main__":
    app.run(debug=True)
