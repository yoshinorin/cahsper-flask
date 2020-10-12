from flask import Blueprint, jsonify
from cahsper.utils.logger import http_request_logging

module_status = Blueprint('status', __name__)

@module_status.route("/status", methods=['GET'], strict_slashes=False)
@http_request_logging
def status():
    return jsonify({"status":"operational"})
