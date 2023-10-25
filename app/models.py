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