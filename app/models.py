from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Post(db.Model):
    STATIC_FOLDER = "posts/images"
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    body = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    @property
    def get_image_url(self):
        return url_for('static', filename=f'{self.STATIC_FOLDER}/{self.image}')
    
    @property
    def get_show_url(self):
        return url_for('posts.post-detials', id=self.id)
    
    @property
    def get_delete_url(self):
        return url_for('posts.post-delete', id=self.id)
    
    @property
    def get_edit_url(self):
        return url_for('posts.post-edit', id=self.id)
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()
    
    def save_edited_post(self):
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()


class Category(db.Model):
    STATIC_FOLDER = "categories/images"
    __tablename__='category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    posts = db.relationship('Post', backref='category_name', lazy=True)

    @property
    def get_show_url(self):
        return url_for('categories.category-detials', id=self.id)
    
    @property
    def get_delete_url(self):
        return url_for('categories.category-delete', id=self.id)
    
    @property
    def get_edit_url(self):
        return url_for('categories.category-edit', id=self.id)
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()
    
    def save_edited_category(self):
        db.session.commit()

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()