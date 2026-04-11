"""
APPLICATION FACTORY PATTERN
"""

from flask import Flask
from flask_cors import CORS
from config import config

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    return app