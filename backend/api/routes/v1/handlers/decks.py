from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from api.depends import get_decks_service
from api.routes.v1.handlers.models import (
    GetDecksResponse, AddDeckRequest, AddDeckResponse, GetDeckResponse
)
from api.auth import check_auth
from src.service.decks import (
    DecksService, DecksAlreadyExistsError
)

router = APIRouter()


@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=GetDecksResponse,
    response_model_exclude_none=True
)
async def get_decks(
        decks_service: DecksService = Depends(get_decks_service)
):
    decks = await decks_service.get_decks()
    return decks


@router.get(
    '/{deck_id}',
    status_code=status.HTTP_200_OK,
    response_model=GetDeckResponse,
    response_model_exclude_none=True
)
async def get_deck(
        deck_id: int,
        decks_service: DecksService = Depends(get_decks_service)
):
    deck = await decks_service.get_deck(deck_id=deck_id)
    return deck


@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=AddDeckResponse
)
async def add_deck(
        deck: AddDeckRequest,
        decks_service: DecksService = Depends(get_decks_service),
        api_key: APIKeyHeader = Depends(check_auth),  # noqa
):
    try:
        deck_id = await decks_service.add_deck(deck)
    except DecksAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.detail)
    return AddDeckResponse(id=deck_id)
