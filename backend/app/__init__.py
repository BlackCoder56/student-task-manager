from flask import Flask
from flask_migrate import Migrate
from app.auth import auth_bp
from app.extensions import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.register_blueprint(auth_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models  # Import models to register them with SQLAlchemy

    return app