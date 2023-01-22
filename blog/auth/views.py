from flask import request, render_template, url_for, redirect
from flask import Blueprint, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required
from blog.models.user import User


auth_app = Blueprint("auth_app", __name__, static_folder='../static', url_prefix='/auth')

login_manager = LoginManager()
login_manager.login_view = 'auth_app.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("authapp.login"))


__all__ = [
    "login_manager",
    "auth_app",
]

@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/auth.html")
    username = request.form.get("username")
    if not username:
        return render_template("auth/auth.html", error="username not passed")
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template("auth/auth.html", error=f'no user {username!r} found')
    login_user(user)
    return redirect(url_for("user_app.users"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect((url_for("user_app.users")))


@auth_app.route("/secret/", endpoint='secret')
@login_required
def secret_view():
    return "Super secret data"
