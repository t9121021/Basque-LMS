import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.main.routes import main
    from app.auth.routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app
