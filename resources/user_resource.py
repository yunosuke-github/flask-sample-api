from flask_restful import Resource

from entity.user import User


class UserResource(Resource):

    def get(self):
        user = User(id=1, name="SAMPLE_01")
        return user.to_json()
