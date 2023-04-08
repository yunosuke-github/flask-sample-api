from flask import Flask
from flask_restful import Api
from resources.user_resource import UserResource
from resources.item_resource import ItemResource


app = Flask(__name__)
api = Api(app)
api.add_resource(UserResource, "/users")
api.add_resource(ItemResource, "/items")

if __name__ == "__main__":
    app.run(debug=True)
