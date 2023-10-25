from flask import Flask
from app.models import  db
from app.config import projectConfig as AppConfig
from flask_migrate import Migrate

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(current_config)
    POSTS_STATIC_FOLDER = "static/posts/images"
    app.config['POSTS_UPLOAD_FOLDER'] = POSTS_STATIC_FOLDER
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)


    from app.posts import posts_blueprint
    app.register_blueprint(posts_blueprint)





    return app