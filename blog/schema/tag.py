from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class TagSchema(Schema):
    class Meta:
        type_ = "tag"
        self_url = "tag_detail"
        self_url_kwargs = {'id': "<id>"}
        self_url_many = "tag_list"

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)
    articles = Relationship(
        nested="ArticleSchema",
        attribute="article",
        related_view="article_detail",
        related_view_kwargs={"id": "<id>"},
        schema="ArticleSchema",
        type_="article",
        many=False,
    )