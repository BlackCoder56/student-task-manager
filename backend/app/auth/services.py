def register_user(data):
    required_fields = ["username", "email", "password"]

    for field in required_fields:
        if not data.get(field):
            return {
                "message": f"{field} is required."
            }, 400

    return {
        "message": "Validation passed!"
    }, 200