from flask import request, jsonify
from app.auth import auth_bp

@auth_bp.route("/register", methods=["POST"])
def register():
    return jsonify({
        "message": "Register endpoint is working!"
    }), 200