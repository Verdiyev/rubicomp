from flask import Flask
from .database import db
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    with app.app_context():
        from .api import api_bp
        app.register_blueprint(api_bp)
        db.create_all()

    return app
