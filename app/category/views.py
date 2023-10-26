from app.category import categories_blueprint
from flask import request, render_template, redirect, url_for
from app.models import Category

@categories_blueprint.route('/hello')
def helloworld():
    return '<h1> Hello world categories </h1>'


@categories_blueprint.route('',endpoint='categories')
def categories():
    categories = Category.query.all()
    return render_template('categories/categories.html', categories=categories)

# -------------------------------------------------------------------------------

# Add New Category
@categories_blueprint.route('/add_new_category', endpoint='category-add', methods=['GET', 'POST'])
def addnewcategory():
    if request.method == 'POST':
        filename = None
        category = Category(title=request.form['title'], body=request.form['body'], image=filename)
        category.save_category()
        return redirect(url_for('categories.categories'))
    return render_template('categories/addnewcategory.html')

# -------------------------------------------------------------------------------

# Post details Page
@categories_blueprint.route('/category/<int:id>', endpoint='category-detials')
def category_details(id):
    category = Category.query.get_or_404(id)
    if category:
        return render_template('categories/category_details.html',category=category)
    else:
        return '<h1> Object not found </h1>', 404

# -------------------------------------------------------------------------------

# Delete Post 
@categories_blueprint.route('/category/<int:id>/delete', endpoint='category-delete')
def post_delete(id):
    category = Category.query.get_or_404(id)
    if category:
        category.delete_category()
        return redirect(url_for('categories.categories'))

# -------------------------------------------------------------------------------

# Edit Post
@categories_blueprint.route('/category/<int:id>/edit', endpoint='category-edit', methods=['GET', 'POST'])
def editpost(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.save_edited_category()
        return redirect(category.get_show_url)
    return render_template('categories/editcategory.html', category=category)