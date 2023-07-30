from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.schema import TagSchema
from blog.extensions import db
from blog.models import Tag


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag
    }