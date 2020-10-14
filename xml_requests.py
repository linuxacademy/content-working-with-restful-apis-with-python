import sys
import requests
import datetime

import defusedxml.ElementTree as ET

from xml.etree.ElementTree import Element, SubElement
from xml.dom.minidom import parseString


def user_element_to_dict(user_element):
    return {
        "user_id": user_element.get("id"),
        "name": user_element.findtext("name"),
        "occupation": user_element.findtext("occupation"),
        "birthday": datetime.date.fromisoformat(user_element.findtext("birthday")),
    }


def parse_user_xml(user_xml):
    root = ET.fromstring(user_xml)

    if root.tag.lower() == "users":
        return [user_element_to_dict(user) for user in root.findall("user")]
    else:
        return user_element_to_dict(root)


def create_user_xml(user_id=None, name=None, occupation=None, birthday=None):
    root = Element("user")

    if user_id:
        root.set("id", str(user_id))

    name_tag = SubElement(root, "name")
    name_tag.text = str(name or "Lance Armstrong")

    occupation_tag = SubElement(root, "occupation")
    occupation_tag.text = str(occupation or "Cyclist")

    birthday_tag = SubElement(root, "birthday")
    birthday_tag.text = str(birthday or "2000-01-01")

    return root


def pretty_xml(root):
    xml_string = ET.tostring(root)
    dom = parseString(xml_string)
    return dom.toprettyxml(encoding="UTF-8")


if __name__ == "__main__":
    order = sys.argv[1].lower()

    user = None
    users = None

    if order == "get_xml":
        resp = requests.get("http://localhost:5000/api/xml/users/1")
        user = parse_user_xml(resp.text)
    elif order == "list_xml":
        resp = requests.get("http://localhost:5000/api/xml/users")
        users = parse_user_xml(resp.text)
    elif order == "create_xml":
        body = pretty_xml(create_user_xml())
        resp = requests.post("http://localhost:5000/api/xml/users/new", data=body)
        user = parse_user_xml(resp.text)
    elif order == "update_xml":
        body = pretty_xml(
            create_user_xml(1, "Bob Barker", "TV Show Host", "1923-12-12")
        )
        resp = requests.put("http://localhost:5000/api/xml/users/1", data=body)
        user = parse_user_xml(resp.text)
    elif order == "delete_xml":
        resp = requests.delete("http://localhost:5000/api/xml/users/1")
        user = parse_user_xml(resp.text)
    else:
        print("Invalid command")
        sys.exit(1)

    print(resp.status_code)
    print(resp.text)

    if user:
        print(user)

    if users:
        print(users)
