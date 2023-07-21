from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
flask_bcrypt = Bcrypt()


__all__ = ["db", "migrate", "login_manager", "flask_bcrypt"]