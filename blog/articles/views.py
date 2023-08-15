from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound
from blog.models import Articles, Author, Tag
from blog.forms import CreateArticleForm
from blog.extensions import db
from sqlalchemy.orm import joinedload
import requests

article_app = Blueprint('article_app', __name__, static_folder='../static', url_prefix='/articles')

# ARTICLES = {
#     1: {
#         'name': 'article 1',
#         'text': 'text 1',
#         'author': 1,
#     },
#     2: {
#         'name': 'article 2',
#         'text': 'text 1',
#         'author': 1
#     }
# }


@article_app.route('/', endpoint='article')
def articles_list():
    articles = Articles.query.all()
    count = requests.get('http://0.0.0.0:5000/api/article/event_get_data/')
    return render_template('articles/list.html', articles=articles, count=count.json())


@article_app.route('/create/', methods=['GET', 'POST'], endpoint='article_create')
@login_required
def articles_create():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == 'POST' and form.validate_on_submit():
        article = Articles(
            title=form.title.data,
            description=form.description.data
        )
        db.session.add(article)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for i in selected_tags:
                article.tags.append(i)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.commit()
        except:
            current_app.logger.exception("Could not create")
            error = "Could not create"
        else:
            return redirect(url_for('article_app.article'))
    return render_template('articles/create_articles.html', form=form, error=error)


@article_app.route('/<int:pk>/', endpoint='detail_article')
def get_article(pk: int):
    articles = Articles.query.filter_by(id=pk).options(joinedload(Articles.tags)).one_or_none()
    if articles is None:
        NotFound('This article is not in the database')
    return render_template('articles/detail.html', articles=articles)


@article_app.route('/filter_tag/<string:tag>/', endpoint='article_filter_tag')
def get_articles_tag(tag: str):
    tag_obj = Tag.query.filter_by(name=tag).one_or_none()
    if tag is None:
        NotFound('This tag is not in the database')
    first_articles = Articles.query.all()
    articles = []
    for i in first_articles:
        if tag_obj not in i.tags:
            NotFound('This article is not with this tag')
        else:
            articles.append(i)
    return render_template('articles/list.html', articles=articles)
