from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECREY_KEY'] = 'key'

    from .index import index
    app.register_blueprint(index, url_prefix='/')


    return app