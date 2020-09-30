import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

cahsper = Flask(__name__)

# TODO: stop hard-code
cahsper.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(cahsper)

try:
    os.makedirs(cahsper.instance_path)
except OSError:
    pass

from cahsper.routes.api_status import module_status
from cahsper.routes.users import module_users

cahsper.register_blueprint(module_status)
cahsper.register_blueprint(module_users)
