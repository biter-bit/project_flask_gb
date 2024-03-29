from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.schema import AuthorSchema
from blog.extensions import db
from blog.models import Author


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }