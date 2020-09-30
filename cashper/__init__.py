import os

from flask import Flask

cashper = Flask(__name__)

# TODO: stop hard-code
cashper.config.from_object('config.DevelopmentConfig')

try:
    os.makedirs(cashper.instance_path)
except OSError:
    pass

from cashper.routes.api_status import module_status

cashper.register_blueprint(module_status)
