from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.schema import ArticleSchema
from blog.extensions import db
from blog.models import Articles


class ArticleList(ResourceList):
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
    }