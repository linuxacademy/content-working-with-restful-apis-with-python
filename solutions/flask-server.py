import datetime
import json
from flask import Flask, make_response, request

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

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contact):
            return obj.__dict__

        return super().default(obj)

contact_date = (datetime.date.today() + datetime.timedelta(days=-2))
contacts = {
    "1": Contact("1", "Bugs Bunny", "1 Carrot Lane, Toontown", "carots", contact_date.isoformat()),
    "2": Contact("2", "Sylvester", "5 Alleyway, Toontown", "Tweety", contact_date.isoformat()),
}

@app.route('/api/contacts/all', methods=['GET'])
def get_contacts():
    return json.dumps(contacts, cls=CustomEncoder)


@app.route('/api/contacts/<contact_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def contact(contact_id):
    if request.method == 'GET':
        return json.dumps(contacts[(contact_id)], cls=CustomEncoder), 200
    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.get_json())
        contacts[contact_id].update(**data)
        return json.dumps(contacts[contact_id], cls=CustomEncoder), 200
    else:
        del contacts[contact_id]
        return get_contacts()

@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
