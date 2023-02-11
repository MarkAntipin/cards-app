import typing as tp

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.dal.db.models import DecksModel, CardsModel


# =========== decks ===========

GetDeckResponse = pydantic_model_creator(
    DecksModel,
    name="GetDeck",
)


class GetDecksResponse(BaseModel):
    __root__: tp.List[GetDeckResponse]


AddDeckRequest = pydantic_model_creator(
    DecksModel,
    name="AddDeck",
    exclude=("id",),
)


class AddDeckResponse(BaseModel):
    id: int

# =========== cards ===========


GetCardResponse = pydantic_model_creator(
    CardsModel,
    name="GetCard",
)


class GetCardsResponse(BaseModel):
    __root__: tp.List[GetCardResponse]


class AddCardRequest(BaseModel):
    deck_id: int
    text: str
    sub_text: tp.Optional[str]


class AddCardResponse(BaseModel):
    id: int
