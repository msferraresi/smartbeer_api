from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.recipe_model import Recipe, database, RecipeSchema

app = Blueprint('recipe', __name__, url_prefix='/recipe')
schema = RecipeSchema()