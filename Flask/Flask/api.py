## put and delete - HTTP verbs
### working with API'S --- Json
from flask import Flask,jsonify,request
app = Flask(__name__)

## initial data in my to do list
items = [
    {"id": 1,"name":"Item 1","description":"this is item 1"},
    { "id": 2,"name":"Item 2","description":"this is item 2"}
]

@app.route('/')
def home():
    return "welceme to the sample To Do List"
## Get : Retrieve all the items

@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)

## retrieve a specific item by ID
@app.route('/items/<int:item_id>',methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)

## post request
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item = {
        "id":items[-1]["id"]+1 if items else 1
        ,"name":request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


if __name__ == '__main__':
    app.run(debug = True)
## Put : we update an existing item
@app.route('/items/<int:item_id>',methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name'] = request.json.get('name',item['name'])
@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"]!= item_id]
    return jsonify({"resul":"Item deleted"})