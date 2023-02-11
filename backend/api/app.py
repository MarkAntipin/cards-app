import logging

from backend_utils.server import register_routers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from api.middlewares.errors import ErrorsMiddleware
from api.middlewares.logging import LoggingMiddleware
from api.routes.v1.app import v1_routers
from settings import app_settings, TORTOISE_CONFIG
from src.utils.logging.init_logger import init_logger

logger = logging.getLogger(app_settings.TITLE)


def setup_middlewares(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(ErrorsMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_events(app: FastAPI):
    def log_running():
        if not app_settings.IS_DEBUG:
            logger.info(f'Server running on http://0.0.0.0:{app_settings.PORT}')

    app.add_event_handler("startup", log_running)


def setup_tortoise(app: FastAPI):
    register_tortoise(
        app=app,
        config=TORTOISE_CONFIG,
        generate_schemas=False
    )


def create_app() -> FastAPI:
    init_logger(
        name=app_settings.TITLE,
        is_debug=app_settings.IS_DEBUG
    )
    app = FastAPI(
        title=app_settings.TITLE,
        version=app_settings.VERSION,
    )
    setup_middlewares(app)
    setup_events(app)
    setup_tortoise(app)

    register_routers(
        app=app,
        routers=[*v1_routers]
    )
    return app
