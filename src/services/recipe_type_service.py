from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.recipe_type_model import RecipeType, database, RecipeTypeSchema

app = Blueprint('recipe_type', __name__, url_prefix='/recipe_type')
schema = RecipeTypeSchema()
