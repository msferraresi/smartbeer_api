from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.role_model import Role, database, RoleSchema

app = Blueprint('role', __name__, url_prefix='/role')
schema = RoleSchema()
