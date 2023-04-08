import json
from app import app


def test_get_item():
    response = app.test_client().get("/items")

    assert response.status_code == 200

    user = json.loads(response.json)
    assert user["id"] == 1
    assert user["name"] == "ITEM_01"
    assert user["price"] == 1000
