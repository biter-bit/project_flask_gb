from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.schema import UserSchema
from blog.extensions import db
from blog.models import User

from blog.permissions.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        'permission_get': [UserPermission],
    }