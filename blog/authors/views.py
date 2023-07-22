from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import Author

author_app = Blueprint("author_app", __name__, static_folder='../static', url_prefix='/authors')


@author_app.route('/', endpoint='authors')
def author_list():
    authors = Author.query.all()
    return render_template("authors/list.html", authors=authors)