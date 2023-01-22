from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import User

user_app = Blueprint("user_app", __name__, static_folder='../static', url_prefix='/users')

# USERS = {
#     1: {
#         'name': "James",
#         'article': 1
#     },
#     2: {
#         'name': "Piter",
#         'article': 1
#     },
#     3: {
#         'name': "Max",
#         'article': 1
#     },
#     4: {
#         'name': "Nina",
#         'article': 1
#     },
#     5: {
#         'name': "Misha",
#         'article': 1
#     },
# }


@user_app.route('/', endpoint='users')
def users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@user_app.route('/<int:pk>/', endpoint='detail_user')
def get_user(pk: int):
    try:
        user = User.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound('This user is not in the database')
    return render_template("users/detail.html", users=user)