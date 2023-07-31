from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.api.article import ArticleList, ArticleDetail
from blog.api.author import AuthorList, AuthorDetail
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    event_plugin = EventPlugin()
    permission_plugin = PermissionPlugin()
    api = Api(
        app,
        plugins=[
            api_spec_plugin,
            event_plugin,
            permission_plugin,
        ],
    )
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
    api.route(ArticleList, "article_list", "/api/article/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/article/<int:id>/", tag="Article")

    return api