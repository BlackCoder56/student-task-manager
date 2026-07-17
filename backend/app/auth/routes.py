from flask import request, jsonify
from app.auth import auth_bp
from app.auth.services import register_user

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    result, status = login_user(data)

    return jsonify(result), status

@auth_bp.route("/register", methods=["POST"])
def register():
    
    data = request.get_json()

    result, status = register_user(data)

    return jsonify(result), status