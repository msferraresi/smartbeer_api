from re import template
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import find_modules
from werkzeug.utils import find_modules, import_string
from flasgger import Swagger
from config.swagger import template, swagger_config

database = SQLAlchemy()
marshmallow = Marshmallow()


def create_app(environment=None):
    app = Flask(__name__)


    if environment is None:
        environment = 'development'
    app.config.from_pyfile('./config/{}.py'.format(environment))

    marshmallow.init_app(app)
    database.init_app(app)
    Swagger(app, config=swagger_config, template=template)
    with app.app_context():
        register_blueprint(app)
        database.create_all()

    return app

def register_blueprint(app):
    for module in find_modules('services'):
        app.register_blueprint(import_string(module).app)

