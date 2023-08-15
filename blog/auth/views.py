from flask import request, render_template, url_for, redirect, current_app
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from blog.models import User
from blog.extensions import login_manager, db
from blog.forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound


# создаем блупринт
auth_app = Blueprint("auth_app", __name__, static_folder='../static', url_prefix='/auth')

# указываем view для авторизации
login_manager.login_view = 'auth_app.login'


@login_manager.user_loader
def load_user(user_id):
    """
    Вытаскивает текущего пользователя из базы данных
    """
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    """
    Перенаправляет неавторизированного пользователя на страницу авторизации
    """
    return redirect(url_for("auth_app.login"))


@auth_app.route("/register/", methods=["GET", "POST"], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect("user_app.users")

    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not uniq')
            render_template("auth/register.html", form=form)
        if User.query.filter_by(username=form.username.data).count():
            form.email.errors.append('username not uniq')
            render_template("auth/register.html", form=form)

        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data,
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.exception("Created user %s", user)
            login_user(user)
            return redirect(url_for("user_app.users"))

    return render_template("auth/register.html", form=form, error=error)


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect("user_app.users")

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form, error="username doesn't exist")
        if user.validate_password(form.password.data):
            return render_template("auth/login.html", form=form, error="unvalid username or password")

        login_user(user)
        return redirect(url_for("user_app.users"))

    return render_template("auth/login.html", form=form)


@auth_app.route("/login-as/", methods=["GET", "POST"], endpoint="login-as")
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound
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


__all__ = [
    "auth_app",
]