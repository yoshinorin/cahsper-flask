import os

from flask import Flask

cahsper = Flask(__name__)

# TODO: stop hard-code
cahsper.config.from_object('config.DevelopmentConfig')

try:
    os.makedirs(cahsper.instance_path)
except OSError:
    pass

from cahsper.routes.api_status import module_status

cahsper.register_blueprint(module_status)
