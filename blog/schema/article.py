from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class ArticleSchema(Schema):
    class Meta:
        type_ = "article"
        self_url = "article_detail"
        self_url_kwargs = {'id': '<id>'}
        self_url_many = "article_list"

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False)
    description = fields.String(allow_none=False)
    dt_created = fields.DateTime(allow_none=False)
    dt_updated = fields.DateTime(allow_none=False)

    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_view="author_detail",
        related_view_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )

    tags = Relationship(
        nested="TagSchema",
        attribute="tags",
        related_view="tag_detail",
        related_url_kwargs={"id": "<id>"},
        schema="TagSchema",
        type_="tag",
        many=True,
    )

