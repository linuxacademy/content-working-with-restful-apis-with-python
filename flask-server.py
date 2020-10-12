from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": "Bugs Bunny",
        "address": "12 Rabbit Lane, Hareland, USA",
        "fav-food": "carots"
    },
    {
        "id": 2,
        "name": "Sylvester",
        "address": "45 Tuxedo Court, Catopia, UK",
        "fav-food": "Tweety Bird"
    }

]

@app.route('/', methods=['GET'])
def get_contacts():
    return jsonify({'contacts': contacts})

@app.route('/', methods=['POST'])
def create_contacts():
    new_contact = {
        "id": contacts[-1]['id'] + 1,
        "name": request.json.get("name", ""),
        "address": request.json.get("address", ""),
        "fav-food": request.json.get("fav-food", ""),
    }
    contacts.append(new_contact) 
    return new_contact

@app.route('/', methods=['PATCH'])
def patch_contacts():

    data = request.get_json()
    for contact in contacts:
        if contact['id'] == data['id']:
            for k, v in data.items():
                contact[k] = v
    
    return jsonify({'contacts': contacts})

@app.route('/', methods=['DELETE'])
def delete_contact():

    data = request.get_json()
    for i in range(len(contacts)):
        if contacts[i]['id'] == data['id']:
            del contacts[i]
    
    return jsonify({'contacts': contacts})

@app.route('/', methods=['PUT'])
def put_contact():

    data = request.get_json()
    for i in range(len(contacts)):
        if contacts[i]['id'] == data['id']:
            contacts[i]["name"] = data.get("name")
            contacts[i]["address"] = data.get("address")
            contacts[i]["fav-food"] = data.get("fav-food")
            contacts[i]["name"] = data.get("name")
    
    return jsonify({'contacts': contacts})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
