from flask import Flask
from blog.users.views import user_app
from blog.articles.views import article_app
from blog.auth.views import auth_app
from blog.authors.views import author_app
from blog.extensions import login_manager, db, migrate, flask_bcrypt
import os
from flask_migrate import Migrate


def register_blueprints(app: Flask):
    """
    Регистрирует блупринты (вьюхи)

    :param app: obj
        обьект точки входа приложения
    :return: 'Ok'
    """
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth_app)
    app.register_blueprint(author_app)
    return 'Ok'


def create_app() -> Flask:
    """
    Создает точку входа приложения

    :return: obj
        точку входа приложения
    """
    app = Flask(__name__)
    # пытаемся из переменной окружения "CONFIG_NAME" достать значение или добавить имя "DevConfig"
    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    # добавляем конфигурацию из выбранного пути
    app.config.from_object(f'blog.config.{cfg_name}')
    # инициализируем все утилиты (базу данных, миграции, менеджер логинов, хеширование)
    db.init_app(app)
    migrate.init_app(app=app, db=db, compare_type=True)
    login_manager.init_app(app)
    flask_bcrypt.init_app(app)
    register_blueprints(app)
    return app