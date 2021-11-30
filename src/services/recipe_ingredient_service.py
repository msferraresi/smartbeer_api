from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.recipe_ingredient_model import RecipeIngredient, database, RecipeIngredientSchema

app = Blueprint('recipe_ingredient', __name__, url_prefix='/recipe_ingredient')
schema = RecipeIngredientSchema()