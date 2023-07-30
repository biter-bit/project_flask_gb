from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class UserSchema(Schema):
    class Meta:
        type_ = "user"
        self_url = "user_detail"
        self_url_kwargs = {'id': '<id>'}
        self_url_many = "user_list"

    id = fields.Integer(as_string=True)
    first_name = fields.String(allow_none=False)
    last_name = fields.String(allow_none=False)
    username = fields.String(allow_none=False)
    email = fields.String(allow_none=False)
    is_staff = fields.Boolean(allow_none=False)

    author = Relationship(
        nested="AurhorSchema",
        attribute="author",
        related_view="author_detail",
        related_view_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )