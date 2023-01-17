from flask import Flask
from blog.users.views import user_app
from blog.articles.views import article_app


def register_blueprints(app: Flask):
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app
