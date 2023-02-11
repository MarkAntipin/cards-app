# image-service
Serve to serve images

## Run app
add `.env` file in the project directory

### Without Docker
```bash
poetry install
poetry run aerich init -t settings.TORTOISE_CONFIG
poetry run aerich init-db
poetry run uvicorn run:app --host 0.0.0.0 --port 8080 --workers 1
```

## Migrations
```bash
poetry run aerich migrate --name migration_name
poetry run aerich upgrage
```

## API
docs available on ```http://0.0.0.0:8080/docs```
