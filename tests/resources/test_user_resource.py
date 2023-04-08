import json
from app import app


def test_get_user():
    response = app.test_client().get("/users")

    assert response.status_code == 200

    user = json.loads(response.json)
    assert user["id"] == 1
    assert user["name"] == "SAMPLE_01"
