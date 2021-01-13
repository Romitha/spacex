# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.satellite_controller import api as satellite_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SPACE-X',
          version='1.0',
          description='API for manage satellite'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(satellite_ns, path='/satellite')