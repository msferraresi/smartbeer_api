from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.recipe_configuration_model import RecipeConfiguration, database, RecipeConfigurationSchema

app = Blueprint('recipe_configuration', __name__, url_prefix='/recipe_configuration')
schema = RecipeConfigurationSchema()