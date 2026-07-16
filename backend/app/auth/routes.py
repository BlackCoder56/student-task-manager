from flask import request, jsonify
from app.auth import auth_bp

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    return jsonify(data), 200