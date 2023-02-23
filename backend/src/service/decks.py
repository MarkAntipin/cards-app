import typing as tp

from tortoise.exceptions import IntegrityError

from src.dal.db.models import DecksModel
from api.routes.v1.handlers.models import AddDeckRequest, UpdateDeckRequest


class DeckAlreadyExistsError(Exception):

    def __init__(self):
        self.detail = 'Deck already exists'


class DeckDoesNotExistsError(Exception):

    def __init__(self):
        self.detail = "Deck doesn't exist"


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
            raise DeckAlreadyExistsError()
        return deck.id

    @staticmethod
    async def update_deck(deck: UpdateDeckRequest, deck_id: int) -> int:
        deck = deck.dict(exclude_unset=True)
        deck_to_patch = await DecksModel.get_or_none(id=deck_id)
        if not deck_to_patch:
            raise DeckDoesNotExistsError()
        await deck_to_patch.update_from_dict(deck)
        await deck_to_patch.save()
        return deck_to_patch.id
