from backend_utils.server import Router, compile_routers

from api.routes.v1.handlers import decks
from api.routes.v1.handlers import cards


routers = [
    Router(router=decks.router, tags=['Decks'], prefix='/decks'),
    Router(router=cards.router, tags=['Cards'], prefix='/cards')
]


v1_routers = compile_routers(
    routers=routers,
    root_prefix='/api/v1'
)
