from flask import Blueprint, jsonify
from cahsper.models.comments import Comments

module_comments = Blueprint('comments', __name__)

@module_comments.route("/comments", methods=['GET'])
def get_comments():
    comments = Comments.get_all()
    return jsonify(comments)

