from tortoise.models import Model
from tortoise import fields


class BaseTortoiseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

    class PydanticMeta:
        exclude = ["updated_at", "created_at"]


class DecksModel(BaseTortoiseModel):
    title = fields.CharField(max_length=512, null=False, unique=True)
    description = fields.TextField(null=True)
    color = fields.CharField(max_length=512, null=False, unique=False, default='#FFFFFF')

    class Meta:
        table = "decks"


class CardsModel(BaseTortoiseModel):
    deck = fields.ForeignKeyField("models.DecksModel", null=False)
    text = fields.TextField(null=False)
    sub_text = fields.TextField(null=True)

    class Meta:
        table = "cards"
