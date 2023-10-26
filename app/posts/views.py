from flask import Flask, request, render_template, redirect, url_for
from app.posts import posts_blueprint
from app.models import Post
from werkzeug.utils import secure_filename
import os
from flask import current_app


@posts_blueprint.route('/hello')
def helloworld():
    return '<h1> Hello world </h1>'

# Home Page : All Posts
@posts_blueprint.route('', endpoint='posts')
def posts():
    posts = Post.query.all()
    return render_template('posts/posts.html',posts=posts)

# -------------------------------------------------------------------------------

# Add New Post
@posts_blueprint.route('/add_new_post', endpoint='post-add', methods=['GET', 'POST'])
def addnewpost():
    if request.method == 'POST':
        filename = None
        if 'image' in request.files:
            file = request.files['image']
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(current_app.config['POSTS_UPLOAD_FOLDER'], filename)
                file.save(file_path)
        post = Post(title=request.form['title'], body=request.form['body'], image=filename)
        post.save_post()
        return redirect(url_for('posts.posts'))
    return render_template('posts/addnewpost.html')

# -------------------------------------------------------------------------------

# Post details Page
@posts_blueprint.route('/post/<int:id>', endpoint='post-detials')
def post_details(id):
    post = Post.query.get_or_404(id)
    if post:
        return render_template('posts/posts_details.html',post=post)
    else:
        return '<h1> Object not found </h1>', 404

# -------------------------------------------------------------------------------

# # Delete Post 
@posts_blueprint.route('/post/<int:id>/delete', endpoint='post-delete')
def post_delete(id):
    post = Post.query.get_or_404(id)
    if post:
        post.delete_post()
        return redirect(url_for('posts.posts'))

# -------------------------------------------------------------------------------

# Edit Post
@posts_blueprint.route('/post/<int:id>/edit', endpoint='post-edit', methods=['GET', 'POST'])
def editpost(id):
    post = Post.query.get_or_404(id)
    filename = None
    if request.method == 'POST':
        post.title = request.form['title']
        post.body = request.form['body']
        if 'image' in request.files:
            file = request.files['image']
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(current_app.config['POSTS_UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(file_path)
        post.image = filename
        post.save_edited_post()
        return redirect(post.get_show_url)
    return render_template('posts/editpost.html', post=post)