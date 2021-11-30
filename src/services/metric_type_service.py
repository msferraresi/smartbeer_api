from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.metric_type_model import MetricType, database, MetricTypeSchema

app = Blueprint('metric_type', __name__, url_prefix='/metric_type')
schema = MetricTypeSchema()