from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import APIKeyHeader

from api.depends import get_cards_service
from api.routes.v1.handlers.models import (
    GetCardsResponse, AddCardResponse,
    AddCardRequest, DeleteCardResponse, UpdateCardRequest, UpdateDeckResponse
)
from api.auth import check_auth
from src.service.cards import (
    CardsService, CardsAlreadyExistsError, CardsDoesNotExistsError
)

router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=GetCardsResponse,
    response_model_exclude_none=True
)
async def get_cards(
        cards_service: CardsService = Depends(get_cards_service),
        deck_id: int = Query(...)
):
    cards = await cards_service.get_cards(deck_id=deck_id)
    return cards


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=AddCardResponse
)
async def add_card(
        card: AddCardRequest,
        cards_service: CardsService = Depends(get_cards_service),
        api_key: APIKeyHeader = Depends(check_auth),  # noqa
):
    try:
        card_id = await cards_service.add_card(card)
    except CardsAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.detail)
    return AddCardResponse(id=card_id)


@router.delete(
    '/{card_id}',
    status_code=status.HTTP_200_OK,
    response_model=DeleteCardResponse
)
async def delete_card(
        card_id: int,
        cards_service: CardsService = Depends(get_cards_service),
        api_key: APIKeyHeader = Depends(check_auth),  # noqa
):
    try:
        card_id = await cards_service.delete_card(card_id=card_id)
    except CardsDoesNotExistsError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    return DeleteCardResponse(id=card_id)


@router.patch(
    '/{card_id}',
    status_code=status.HTTP_200_OK,
    response_model=UpdateDeckResponse
)
async def update_card(
        card_id: int,
        card: UpdateCardRequest,
        cards_service: CardsService = Depends(get_cards_service),
        api_key: APIKeyHeader = Depends(check_auth),  # noqa
):
    try:
        card_id = await cards_service.update_card(card=card, card_id=card_id)
    except CardsDoesNotExistsError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    return UpdateDeckResponse(id=card_id)
