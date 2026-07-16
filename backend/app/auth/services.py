from werkzeug.security import generate_password_hash
from app.models import User 
from app.extensions import db

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

    # Hash the password
    hashed_password = generate_password_hash(data["password"])

    # Create a new user
    new_user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password
    )

    db.session.add(new_user) # Add the new user to the session
    db.session.commit() # Commit the changes to the database


    return {
        "message": "User registered successfully."
    }, 201