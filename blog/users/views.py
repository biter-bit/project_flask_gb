from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user_app = Blueprint("user_app", __name__, static_folder='../static', url_prefix='/users')

USERS = {
    1: {
        'name': "James",
        'article': 1
    },
    2: {
        'name': "Piter",
        'article': 1
    },
    3: {
        'name': "Max",
        'article': 1
    },
    4: {
        'name': "Nina",
        'article': 1
    },
    5: {
        'name': "Misha",
        'article': 1
    },
}


@user_app.route('/', endpoint='users')
def users_list():
    return render_template("users/list.html", users=USERS)


@user_app.route('/<int:pk>/', endpoint='detail_user')
def get_user(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        raise NotFound('This user is not in the database')
    return render_template("users/detail.html", users=user)