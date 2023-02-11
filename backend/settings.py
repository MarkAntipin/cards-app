from pathlib import Path

import dotenv
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent

ENV_FILE = Path(BASE_DIR, '.env')
dotenv.load_dotenv(ENV_FILE)


class PostgresSettings(BaseSettings):
    DATABASE_PORT: int = 5432
    DATABASE_HOST: str = 'localhost'
    DATABASE_NAME: str = 'cards-app'
    DATABASE_USER: str = 'cards-app'
    DATABASE_PASSWORD: str = 'postgres'


class AppSettings(BaseSettings):
    PORT: int = 8080
    IS_DEBUG: bool = False

    TITLE: str = 'Cards App'
    VERSION: str = '0.1.0'

    API_KEY: str

    class Config:
        case_sensitive = False


app_settings = AppSettings()
postgres_settings = PostgresSettings()


TORTOISE_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': postgres_settings.DATABASE_HOST,
                'port': postgres_settings.DATABASE_PORT,
                'user': postgres_settings.DATABASE_USER,
                'password': postgres_settings.DATABASE_PASSWORD,
                'database': postgres_settings.DATABASE_NAME,
            },
        }
    },
    'apps': {
        'models': {
            'models': [
                'src.dal.db.models',
                'aerich.models'
            ],
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'UTC',
}
