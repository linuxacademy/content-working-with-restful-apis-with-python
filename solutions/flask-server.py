from flask import Flask, json, jsonify, make_response, request

app = Flask(__name__)

class Contact:
    def __init__(self, contact_id, name, address, favorite_food):
        self.contact_id = contact_id
        self.name = name
        self.address = address
        self.favorite_food = favorite_food
    
    def serialize(self):
        return self.__dict__


contacts = {
    1: Contact("1", "Bugs Bunny", "1 Carrot Lane, Toontown", "carots"),
    2: Contact("2", "Sylvester", "5 Alleyway, Toontown", "Tweety")
}

@app.route('/api/contacts/all', methods=['GET'])
def get_contacts():
    return jsonify(data=[contacts[id].serialize() for id in contacts])


@app.route('/api/contacts/<contact_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def contact(contact_id):
    id = int(contact_id)
    
    if request.method == 'GET':
        return contacts[id].serialize()

@app.route('/api/contacts/new', methods=['POST'])
def create_contact():
    data = request.get_json()
    data["contact_id"] = int(sorted(contacts.keys())[-1]) + 1
    new_contact = Contact(**data)
    contacts[data['contact_id']] = new_contact

    return new_contact.serialize()

# @app.route('/', methods=['PATCH'])
# def patch_contacts():

#     data = request.get_json()
#     for contact in contacts:
#         if contact['id'] == data['id']:
#             for k, v in data.items():
#                 contact[k] = v
    
#     response = app.response_class(
#         response=json.dumps(contacts, indent=2),
#         mimetype='application/json'
#     )
#     return response

# @app.route('/', methods=['DELETE'])
# def delete_contact():

#     data = request.get_json()
#     for i in range(len(contacts)):
#         if contacts[i]['id'] == data['id']:
#             del contacts[i]
    
#     response = app.response_class(
#         response=json.dumps(contacts, indent=2),
#         mimetype='application/json'
#     )
#     return response

# @app.route('/', methods=['PUT'])
# def put_contact():

#     data = request.get_json()
#     for i in range(len(contacts)):
#         if contacts[i]['id'] == data['id']:
#             contacts[i]["name"] = data.get("name")
#             contacts[i]["address"] = data.get("address")
#             contacts[i]["fav-food"] = data.get("fav-food")
#             contacts[i]["name"] = data.get("name")
    
#     return jsonify({'contacts': contacts})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
