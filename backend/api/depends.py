from src.service.decks import DecksService
from src.service.cards import CardsService


def get_decks_service() -> DecksService:
    return DecksService()


def get_cards_service() -> CardsService:
    return CardsService()
