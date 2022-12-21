from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article_app = Blueprint('article_app', __name__, static_folder='../static', url_prefix='/articles')

ARTICLES = {
    1: {
        'name': 'article 1',
        'text': 'text 1',
        'author': 1,
    },
    2: {
        'name': 'article 2',
        'text': 'text 1',
        'author': 1
    }
}


@article_app.route('/', endpoint='article')
def articles_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article_app.route('/<int:pk>/', endpoint='detail_article')
def get_article(pk: int):
    try:
        article = ARTICLES[pk]
    except:
        NotFound('This article is not in the database')
    return render_template('articles/detail.html', articles=article)