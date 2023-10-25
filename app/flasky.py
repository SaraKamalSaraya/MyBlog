from app import create_app
from flask import Flask, render_template

app = create_app('prd')

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('errors/page_not_found.html'), 404

if __name__ == '__main__':
    app.run()