from app.category import categories_blueprint

@categories_blueprint.route('/hello')
def helloworld():
    return '<h1> Hello world categories </h1>'


@categories_blueprint.route('',endpoint='categories')
def categories():
    return '<h1> Hello world categories </h1>'

