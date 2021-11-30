from flask import Blueprint, jsonify

app = Blueprint("ping", __name__, url_prefix="/ping")

@app.route("/", methods=["GET"])
def ping():
    return jsonify(message="pong"), 200
