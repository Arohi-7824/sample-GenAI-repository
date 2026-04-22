import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET KEY')
    DEBUG=os.getenv('FLASK_DEBUG', 'False')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///chatbot.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    GROQ_MODEL = os.getenv('GROQ_MODEL', 'llama3-70b-8192')
    
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    JSON_SORT_KEYS = False

    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///chatbot.db')

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}