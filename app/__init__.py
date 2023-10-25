from flask import Flask
from app.models import  db
from app.config import projectConfig as AppConfig
# from flask_migrate import Migrate

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(current_config)
    db.init_app(app)
    return app