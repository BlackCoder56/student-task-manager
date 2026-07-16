from flask import request, jsonify
from app.auth import auth_bp

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    required_fields = ["username", "email", "password"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "message": f"{field} is required."
            }), 400    

    return jsonify({
        "message": "Validation passed!"
    }), 200