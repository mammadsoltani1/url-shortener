# URL Shortener

A FastAPI service that shortens long URLs and redirects short codes back to the original destination. Short code generation is pluggable (random, hash, or uuid based).

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL

## Setup

Copy the example environment file and adjust it if needed:

```bash
cp .env.example .env
```

Install dependencies:

```bash
uv sync
```

Make sure PostgreSQL is running and reachable at the `DATABASE_URL` from your `.env`, then apply migrations:

```bash
uv run alembic upgrade head
```

## Running the app

```bash
uv run fastapi dev src/url_shortener/main.py
```

The API will be available at `http://localhost:8000`. Interactive docs are at `http://localhost:8000/docs`.

## Configuration

Set these in `.env`:

| Variable | Description | Default |
|---|---|---|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+psycopg2://postgres:postgres@localhost:5432/url_shortener` |
| `SHORTCODE_STRATEGY` | `random`, `hash`, or `uuid` | `hash` |
| `SHORTCODE_LENGTH` | Length of generated short codes | `8` |
| `BASE_URL` | Base URL used to build the returned short link | `http://localhost:8000` |

## API

- `POST /shorten` - shorten a URL. Body: `{"original_url": "https://example.com/some/path"}`
- `GET /{short_code}` - redirect to the original URL
- `GET /health` - health check

## Database migrations

Migrations live in `migrations/`. To create a new one after changing a model:

```bash
uv run alembic revision --autogenerate -m "description"
uv run alembic upgrade head
```
