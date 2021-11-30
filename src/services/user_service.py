from functools import wraps
from flask import Blueprint, request, jsonify
import uuid
import jwt
from werkzeug.security import generate_password_hash

from models.user_model import User, database, UserSchema
from flasgger import swag_from

app = Blueprint('user', __name__, url_prefix='/user')
schema = UserSchema()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, 'smartbeer')
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route("", methods=["GET"])
@token_required
@swag_from("docs/user/get_all.yaml")
def get_all(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    objs = User.query.filter_by(deleted_at=None).all()
    return jsonify(schema.dump(objs, many=True)), 200

@app.route("/<public_id>", methods=["GET"])
@token_required
@swag_from("docs/user/get_by_id.yaml")
def get_byId(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    obj = User.query.filter_by(public_id=public_id, deleted_at=None).first()
    if not obj:
        return jsonify({"message": "User not found"}), 404
    return jsonify(schema.dump(obj)), 200

@app.route("/name/<name>", methods=["GET"])
@token_required
@swag_from("docs/user/get_by_name.yaml")
def get_byName(current_user, name):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    obj = User.query.filter_by(name=name, deleted_at=None).first()
    if not obj:
        return jsonify({"message": "User not found"}), 404
    return jsonify(schema.dump(obj)), 200

@app.route("/email/<email>", methods=["GET"])
@token_required
@swag_from("docs/user/get_by_email.yaml")
def get_byEmail(current_user, email):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
    
    obj = User.query.filter_by(mail=email, deleted_at=None).first()
    if not obj:
        return jsonify({"message": "User not found"}), 404
    return jsonify(schema.dump(obj)), 200    

@app.route("", methods=["POST"])
@token_required
@swag_from("docs/user/post_create.yaml")
def create(current_user):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
        
    obj = schema.load(request.json)
    hashed_password = generate_password_hash(obj.password, method='sha256')
    obj.public_id = str(uuid.uuid4())
    obj.password = hashed_password
    obj.admin = False
    database.session.add(obj)
    database.session.commit()
    return jsonify(schema.dump(obj)), 200

@app.route("/<public_id>", methods=["PUT"])
@token_required
@swag_from("docs/user/put_update.yaml")
def update(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
        
    obj = User.query.filter_by(public_id=public_id, deleted_at=None).first()
    if not obj:
        return jsonify({"message": "User not found"}), 404
    obj = schema.load(request.json, instance=obj)
    database.session.commit()
    return jsonify(schema.dump(obj)), 200

@app.route("/<public_id>", methods=["DELETE"])
@token_required
@swag_from("docs/user/delete_delete.yaml")
def delete(current_user, public_id):
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})
        
    obj = User.query.filter_by(public_id=public_id, deleted_at=None).first()
    if not obj:
        return jsonify({"message": "User not found"}), 404
    obj.deleted_at = database.func.now()
    database.session.commit()
    return jsonify({"message": "User has been deleted"}), 200

