import typing as tp

from tortoise.exceptions import IntegrityError

from src.dal.db.models import DecksModel
from api.routes.v1.handlers.models import AddDeckRequest


class DecksAlreadyExistsError(Exception):

    def __init__(self):
        self.detail = 'Deck already exists'


class DecksService:

    @staticmethod
    async def get_decks() -> tp.List[DecksModel]:
        decks = await DecksModel.all()
        return decks

    @staticmethod
    async def get_deck(deck_id: int) -> tp.Optional[DecksModel]:
        deck = await DecksModel.get_or_none(id=deck_id)
        return deck

    @staticmethod
    async def add_deck(deck: AddDeckRequest) -> int:
        try:
            deck = await DecksModel.create(**deck.dict(exclude_unset=True))
        except IntegrityError:
            raise DecksAlreadyExistsError()
        return deck.id
