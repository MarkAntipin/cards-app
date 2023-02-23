import typing as tp

from tortoise.exceptions import IntegrityError

from src.dal.db.models import CardsModel
from api.routes.v1.handlers.models import AddCardRequest, UpdateCardRequest


class CardsAlreadyExistsError(Exception):

    def __init__(self):
        self.detail = 'Card already exists'


class CardsDoesNotExistsError(Exception):

    def __init__(self):
        self.detail = "Card doesn't exist"


class CardsService:

    @staticmethod
    async def get_cards(deck_id: int) -> tp.List[CardsModel]:
        cards = await CardsModel.filter(deck_id=deck_id).order_by('-id').all()
        return cards

    @staticmethod
    async def add_card(card: AddCardRequest) -> int:
        try:
            card = await CardsModel.create(**card.dict(exclude_unset=True))
        except IntegrityError:
            raise CardsAlreadyExistsError()
        return card.id

    @staticmethod
    async def delete_card(card_id: int) -> int:
        card = await CardsModel.get_or_none(id=card_id)
        if not card:
            raise CardsDoesNotExistsError()
        await card.delete()
        return card.id

    @staticmethod
    async def update_card(card: UpdateCardRequest, card_id: int) -> int:
        card = card.dict(exclude_unset=True)
        card_to_patch = await CardsModel.get_or_none(id=card_id)
        if not card_to_patch:
            raise CardsDoesNotExistsError()
        await card_to_patch.update_from_dict(card)
        await card_to_patch.save()
        return card_to_patch.id
