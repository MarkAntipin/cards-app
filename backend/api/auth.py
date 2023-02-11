from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from settings import app_settings


_AUTHORIZATION_HEADER_NAME = 'Authorization'
_AUTHORIZATION_HEADER = APIKeyHeader(name=_AUTHORIZATION_HEADER_NAME)


def check_auth(token: APIKeyHeader = Depends(_AUTHORIZATION_HEADER)) -> APIKeyHeader:
    if app_settings.API_KEY != token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid authorization header')
    return token
