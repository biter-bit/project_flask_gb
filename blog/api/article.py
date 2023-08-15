from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.schema import ArticleSchema
from blog.extensions import db
from blog.models import Articles

from combojsonapi.event.resource import EventsResource
from blog.permissions.article import ArticlePermission


class ArticleListEvents(EventsResource):
    def event_get_data(self, _permission_user):
        return {"count": Articles.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Articles,
        'permission_get': [ArticlePermission],
        'permission_patch': [ArticlePermission],
    }