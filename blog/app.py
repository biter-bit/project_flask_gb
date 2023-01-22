from flask import Flask
from blog.users.views import user_app
from blog.articles.views import article_app
from blog.auth.views import auth_app, login_manager
from blog.models.database import db


def register_blueprints(app: Flask):
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "abcdefg1234556"
    db.init_app(app)
    login_manager.init_app(app)
    register_blueprints(app)
    return app
