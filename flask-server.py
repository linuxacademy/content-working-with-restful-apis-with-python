import datetime
from flask import Flask, json, jsonify, make_response, request
from flask.json import JSONEncoder, JSONDecoder

app = Flask(__name__)

class Contact:
    def __init__(self, contact_id, name, address, favorite_food, last_contact):
        self.contact_id = contact_id
        self.name = name
        self.address = address
        self.favorite_food = favorite_food
        self.last_contact = last_contact
    
    def update(self, contact_id=None, name=None, address=None, favorite_food=None, last_contact=None, *args, **kwargs):
        if contact_id:
            self.contact_id = contact_id
        if name: 
            self.name = name
        if address:
            self.address = address
        if favorite_food:
            self.favorite_food = favorite_food
        if last_contact:
            self.last_contact = last_contact
    
    def serialize(self):
        return self.__dict__


contact_date = (datetime.date.today() + datetime.timedelta(days=-2))
contacts = {
    "1": Contact("1", "Bugs Bunny", "1 Carrot Lane, Toontown", "carots", contact_date),
    "2": Contact("2", "Sylvester", "5 Alleyway, Toontown", "Tweety", contact_date),
}

@app.route('/api/contacts/all', methods=['GET'])
def get_contacts():
    return jsonify(data=[contacts[id].serialize() for id in contacts]), 200

@app.route('/api/contacts/<contact_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def contact(contact_id):
    if request.method == 'GET':
        return contacts[(contact_id)].serialize(), 200
    elif request.method in ['PUT', 'PATCH']:
        contacts[contact_id].update(**request.get_json())
        return contacts[contact_id].serialize(), 200
    else:
        del contacts[contact_id]
        return get_contacts()

@app.route('/api/contacts/new', methods=['POST'])
def create_contact():
    data = request.get_json()
    data["contact_id"] = str(int(sorted(contacts.keys())[-1]) + 1)
    new_contact = Contact(**data)
    contacts[data['contact_id']] = new_contact
    return new_contact.serialize(), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
