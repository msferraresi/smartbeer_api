from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.user_role_model import UserRole, database, UserRoleSchema

app = Blueprint('user_role', __name__, url_prefix='/user_role')
schema = UserRoleSchema()
