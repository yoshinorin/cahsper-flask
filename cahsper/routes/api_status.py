from flask import Blueprint, jsonify

module_status = Blueprint('status', __name__)

@module_status.route("/status", methods=['GET'])
def status():
    return jsonify({"status":"operational"})
