import typing as tp

from tortoise.exceptions import IntegrityError

from src.dal.db.models import CardsModel
from api.routes.v1.handlers.models import AddCardRequest


class CardsAlreadyExistsError(Exception):

    def __init__(self):
        self.detail = 'Card already exists'


class CardsService:

    @staticmethod
    async def get_cards(deck_id: int) -> tp.List[CardsModel]:
        cards = await CardsModel.filter(deck_id=deck_id).all()
        return cards

    @staticmethod
    async def add_card(card: AddCardRequest) -> int:
        try:
            card = await CardsModel.create(**card.dict(exclude_unset=True))
        except IntegrityError:
            raise CardsAlreadyExistsError()
        return card.id
