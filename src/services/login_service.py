import datetime
from flask import Blueprint, request, jsonify, make_response
import jwt
from models.user_model import User
from werkzeug.security import check_password_hash


app = Blueprint("login", __name__, url_prefix="/login")

@app.route("/", methods=["GET"])
def login():
    
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    user = User.query.filter_by(name=auth.username, deleted_at=None).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'smartbeer')
        return jsonify({'token' : token.decode('UTF-8')})
    
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})



