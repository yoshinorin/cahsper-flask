import json
from flask import Blueprint, Response
from cahsper.models.users import Users

module_users = Blueprint('users', __name__)

@module_users.route("/users/<user_name>", methods=['GET'], strict_slashes=False)
def get_user(user_name):
    user = Users.find_by_name(user_name)
    if not user:
        return Response(json.dumps({"message": "NotFound"}), status=404, content_type='application/json')
    return Response(response=json.dumps(user.serialize()), status=200, content_type='application/json')

@module_users.route("/users", methods=['GET'], strict_slashes=False)
def get_users():
    users = []
    for user in Users.get_all():
        users.append(user.serialize())

    return Response(response=json.dumps(users), status=200, content_type='application/json')
