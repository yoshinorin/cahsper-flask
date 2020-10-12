import json

from flask import Blueprint, Response, request
from cahsper.models.users import Users
from cahsper.models.comments import Comments
from cahsper.auth.cognito import jwt_validator
from cahsper.utils.logger import http_request_logging

module_users = Blueprint('users', __name__)

@module_users.route("/users/<user_name>", methods=['GET'], strict_slashes=False)
@http_request_logging
def get_user(user_name):
    user = Users.find_by_name(user_name)

    if not user:
        return Response(json.dumps({"message": "NotFound"}), status=404, content_type='application/json')
    return Response(response=json.dumps(user.serialize()), status=200, content_type='application/json')

@module_users.route("/users", methods=['GET'], strict_slashes=False)
@http_request_logging
def get_users():
    users = []
    for user in Users.get_all():
        users.append(user.serialize())

    return Response(response=json.dumps(users), status=200, content_type='application/json')

@module_users.route("/users/<user_name>/comments", methods=['GET'], strict_slashes=False)
@http_request_logging
def get_user_comments(user_name):
    comments = []
    for comment in Comments.find_by_username(user_name):
        comments.append(comment.serialize())

    return Response(response=json.dumps(comments), status=200, content_type='application/json')

@module_users.route("/users/<user_name>/comments", methods=['POST'], strict_slashes=False)
@http_request_logging
@jwt_validator
def post_user_comments(user_name, claims):

    return Response(json.dumps({"message": "todo"}), status=404, content_type='application/json')
