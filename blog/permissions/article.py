from combojsonapi.permission.permission_system import (PermissionMixin, PermissionUser, PermissionForGet,
                                                       PermissionForPatch)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from blog.models import User, Articles

import flask


class ArticlePermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        'id',
        'title',
        'description',
        'dt_created',
        'dt_updated',
    ]

    PATCH_AVAILABLE_FIELDS = [
        'title',
        'description',
    ]

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        if not current_user.is_authenticated:
            raise AccessDenied('no access')
        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        article_id = flask.request.view_args.get('id')
        article_obj_user = current_user.author.article
        for i in article_obj_user:
            if current_user.is_staff or article_id == i.id:
                self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
                return self.permission_for_patch
            else:
                raise AccessDenied('no access')

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Articles)
        return {
            k: v for k, v in data.items() if k in permission_for_patch.columns
        }