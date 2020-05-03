from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):

    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)
        return {"itemm": item}, 200 if item else None

    def post(self, name):  #parameter name should match with <string:name>
                            # here not catching the json from body request
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item


class Items(Resource):
    def get(self):
        return {"Items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")

app.run(debug=True, host='0.0.0.0', port=8080)
