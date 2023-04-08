from flask_restful import Resource

from entity.item import Item


class ItemResource(Resource):

    def get(self):
        item = Item(id=1, name="ITEM_01", price=1000)
        return item.to_json()
