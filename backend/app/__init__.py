from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
    
    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        from .routes import register_routes
        register_routes(app)

    return app