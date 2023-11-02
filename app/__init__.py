from flask_restful import Api
from .posts.api_view import PostList, PostResource
from flask import Flask
from app.models import db
from app.config import projectConfig as AppConfig
from flask_migrate import Migrate
from flask import render_template

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(current_config)
    POSTS_STATIC_FOLDER = "static/posts/images"
    app.config['POSTS_UPLOAD_FOLDER'] = POSTS_STATIC_FOLDER
    CATEGORY_STATIC_FOLDER = "static/category/images"
    app.config['CATEGORY_UPLOAD_FOLDER'] = CATEGORY_STATIC_FOLDER
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    api = Api(app)

    api.add_resource(PostList, '/api/posts')
    api.add_resource(PostResource, '/api/posts/<int:post_id>')

    # Contact
    def contactus():
        return render_template('others/contactus.html')

    # About
    def aboutus():
        return render_template('others/aboutus.html')

    app.add_url_rule("/contact-us", view_func=contactus, endpoint='contactus', methods=['GET'])
    app.add_url_rule("/about-us", view_func=aboutus, endpoint='aboutus', methods=['GET'])


    from app.posts import posts_blueprint
    app.register_blueprint(posts_blueprint)

    from app.category import categories_blueprint
    app.register_blueprint(categories_blueprint)


    return app