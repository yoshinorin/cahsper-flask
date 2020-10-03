from flask import Blueprint, jsonify
from cahsper.models.users import Users

module_users = Blueprint('users', __name__)

@module_users.route("/users/<user_name>", methods=['GET'])
def get_user(user_name):
    user = Users.find_by_name(user_name)

    if not user:
        return jsonify({"message": "NotFound"})

    return jsonify(user)

@module_users.route("/users", methods=['GET'])
def get_users():
    users = Users.get_all()

    return jsonify(users)
