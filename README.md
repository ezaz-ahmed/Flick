# Flick

Flick is a video streaming project built to explore production-style Python backend development, video processing, HLS streaming, and adaptive playback.

The backend is built with FastAPI and will gradually include FFprobe, FFmpeg, PostgreSQL, Redis-backed background jobs, HLS generation, and Cloudflare Stream integration.

## Tech Stack

- Python 3.12+
- FastAPI
- uv
- pytest
- Ruff
- mypy

## Project Structure

```text
Flick/
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_health.py
│   ├── pyproject.toml
│   ├── uv.lock
│   └── .python-version
├── .gitignore
└── README.md
```

## Backend Setup

```bash
cd server
uv sync
```

Start the development server:

```bash
uv run fastapi dev app/main.py
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Development

Run tests:

```bash
uv run pytest
```

Run lint checks:

```bash
uv run ruff check .
```

Run type checks:

```bash
uv run mypy app
```

Format code:

```bash
uv run ruff format .
```

## Planned Features

- Video upload API
- Media inspection with FFprobe
- Video processing with FFmpeg
- PostgreSQL persistence
- Background processing with Redis
- Adaptive HLS transcoding
- Cloudflare Stream integration
- Webhook processing
- Retries and idempotent jobs
- Reels-style video feed
- Dockerized development environment
