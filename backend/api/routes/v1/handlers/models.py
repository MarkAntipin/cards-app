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


class UpdateDeckRequest(BaseModel):
    title: tp.Optional[str]
    description: tp.Optional[str]
    color: tp.Optional[str]


class AddDeckResponse(BaseModel):
    id: int


class UpdateDeckResponse(AddDeckResponse):
    pass

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


class UpdateCardRequest(BaseModel):
    deck_id: tp.Optional[int]
    text: tp.Optional[str]
    sub_text: tp.Optional[str]


class AddCardResponse(BaseModel):
    id: int


class DeleteCardResponse(AddCardResponse):
    pass


class UpdateCardResponse(AddCardResponse):
    pass
