from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class AuthorSchema(Schema):
    class Meta:
        type_ = "author"
        self_url = "author_detail"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "author_list"

    id = fields.Integer(as_string=True)

    user = Relationship(
        nested="UserSchema",
        attribute="user",
        related_view="user_detail",
        related_view_kwargs={"id": "<id>"},
        schema="UserSchema",
        type_="user",
        many=False,
    )

    articles = Relationship(
        nested="ArticleSchema",
        attribute="articles",
        related_view="article_detail",
        related_view_kwargs={"id": "<id>"},
        schema="UserSchema",
        type_="user",
        many=False,
    )