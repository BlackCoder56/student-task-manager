from app.models import User 

def register_user(data):

    required_fields = ["username", "email", "password"]

    for field in required_fields:
        if not data.get(field):
            return {
                "message": f"{field} is required."
            }, 400

    existing_username = User.query.filter_by(
        username=data["username"]
    ).first()

    if existing_username:
        return {
            "message": "Username already exists."
        }, 400

    existing_email = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_email:
        return {
            "message": "Email already exists."
        }, 400

    return {
        "message": "Validation passed!"
    }, 200