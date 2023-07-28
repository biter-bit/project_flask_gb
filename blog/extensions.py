from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from blog.admin import MyAdminIndexView

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
flask_bcrypt = Bcrypt()
admin = Admin(name="Blog Admin", template_mode="bootstrap4", index_view=MyAdminIndexView())


__all__ = ["db", "migrate", "login_manager", "flask_bcrypt", "admin"]