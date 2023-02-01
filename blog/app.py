from flask import Flask
from blog.users.views import user_app
from blog.articles.views import article_app
from blog.auth.views import auth_app, login_manager
from blog.models.database import db
import os
from flask_migrate import Migrate


def register_blueprints(app: Flask):
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)


def create_app() -> Flask:
    app = Flask(__name__)
    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    app.config.from_object(f'blog.config.{cfg_name}')
    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    login_manager.init_app(app)
    register_blueprints(app)
    return app
