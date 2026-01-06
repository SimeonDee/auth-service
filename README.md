# Auth Service - SAS School Management System 🚀

[![CI](https://github.com/{owner}/{repo}/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/{owner}/{repo}/actions/workflows/ci.yml) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/{owner}/{repo}/main.svg)](https://results.pre-commit.ci/latest/github/{owner}/{repo}/main) [![codecov](https://codecov.io/gh/{owner}/{repo}/branch/main/graph/badge.svg)](https://codecov.io/gh/{owner}/{repo})

**A production-ready FastAPI Auth Service** built as a solid starting point for web APIs. This project demonstrates a auth setup with JWT authentication, async SQLAlchemy + PostgreSQL, Alembic migrations, Docker support, tests, and a clear service/schema separation.

---

## Table of Contents 📚
- [Features](#features)
- [Quickstart](#quickstart)
- [Environment variables](#environment-variables)
- [Run locally](#run-locally)
- [Run with Docker](#run-with-docker)
- [Database migrations](#database-migrations)
- [Testing & Quality](#testing--quality)
- [API Endpoints & Usage](#api-endpoints--usage)
- [Project Layout](#project-layout)
- [Implementation Notes](#implementation-notes)
- [Production Considerations](#production-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Features ✅
- JWT-based authentication (access token / refresh token pattern ready)
- Role-based user model (`core/user_roles.py`)
- Async SQLAlchemy + PostgreSQL (`app/models`, `app/db/session.py`)
- Alembic for database migrations
- Pydantic schemas for request/response validation (`app/schemas`)
- Service layer pattern (`app/services`) for business logic separation
- Docker + Docker Compose support for local/dev environments
- Tests using `pytest` (see `tests/`)
- OpenAPI / interactive docs via FastAPI (`/docs`, `/redoc`)

---

## Quickstart ⚡
1. Copy the example environment file and edit values:

   ```bash
   cp .env.example .env
   # Edit .env (DATABASE_URL, SECRET_KEY, etc.)
   ```

2. Create a Python virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run Postgres (locally or with Docker) and set `DATABASE_URL` in `.env`.
4. Run migrations (see below) and start the app:

   ```bash
   ./run.sh
   # or
   uvicorn app.main:app --reload
   ```

Open Swagger UI: http://127.0.0.1:8000/docs

Open ReDoc UI: http://127.0.0.1:8000/redoc

---

## Environment variables 🔑
Minimal environment variables used by the project (set in `.env`):

- `DATABASE_URL` — SQLAlchemy database URL (eg. `postgresql+asyncpg://user:pass@db:5432/app_db`)
- `SECRET_KEY` — secret for JWT signing
- `ACCESS_TOKEN_EXPIRE_MINUTES` — expiration time for access tokens
- `JWT_ALGORITHM` — algorithm used for JWT (`HS256` by default)

You can use `.env.example` as a reference.

---

## Run with Docker 🐳
Start dependencies and the app (recommended for local dev):

```bash
# Start Postgres
docker-compose up -d

# Build & run the app container (if you have a Dockerfile defined)
docker-compose up --build app
```

Ensure `DATABASE_URL` in `.env` points to the Docker Postgres service (e.g. `postgresql://postgres:postgres@postgres:5432/app_db`).

---

## Database migrations (Alembic) 🔧
Create and apply migrations:

```bash
# generate migration (autogenerate from models)
alembic revision --autogenerate -m "add users"

# apply migrations
alembic upgrade head
```

Note: `alembic/env.py` is set up to import `app.models` so autogeneration works.

---

## Testing & Quality ✅
Run tests with `pytest`:

```bash
pytest -q
```

Linting / formatting suggestions:
- Use `flake8` / `ruff` for linting
- Use `black` for code formatting

---

## API Endpoints & Usage 🔌
Key auth endpoints (see `app/api/api_v1/auth.py`):

- `POST /api/v1/auth/register` — register new user
- `POST /api/v1/auth/token` — obtain JWT token (OAuth2 password flow)
- `GET /api/v1/users/me` — get current user (requires Bearer token)

Quick example (register + token):

```bash
# Register
curl -s -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"secret"}'

# Get token
curl -s -X POST http://localhost:8000/api/v1/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=secret"
```

Use the returned access token as a Bearer token for protected endpoints.

---

## Project Layout 🗂️
High-level structure (important files/folders):

```
app/
├─ api/           # FastAPI routers
│  └─ api_v1/
├─ core/          # app configuration, jwt helpers, user roles
├─ db/            # session / connection setup
├─ models/        # SQLAlchemy models
├─ schemas/       # Pydantic schemas
├─ services/      # business logic
└─ main.py        # application factory / startup

alembic/          # migrations
tests/             # pytest tests
```

---

## Implementation Notes 🧩
- Authentication: JWT tokens are issued using utilities in `app/core/jwt.py`.
- Business logic lives in `app/services/user_service.py` and controllers in `app/api/api_v1`.
- The project follows an async-first approach using `asyncpg` + SQLAlchemy 1.4+ async APIs.

---

## Production Considerations ⚠️
- Use a robust secrets manager for `SECRET_KEY` (avoid checking secrets into Git).
- Configure connection pooling and database timeouts for production DBs.
- Ensure CORS, rate limiting, and security headers are configured in fronting proxy or in FastAPI middleware.
- Add health checks and readiness probes for orchestration (Kubernetes).
- Enable structured logging and error monitoring (Sentry, Datadog, etc.).

---

## Contributing 🤝
Contributions are welcome — please see `CONTRIBUTING.md` for details on the contribution workflow and PR checklist.

**Quick notes:**
- CI is configured via GitHub Actions to run tests and linters on PRs (`.github/workflows/ci.yml`).
- Pre-commit hooks (black, ruff, isort) are configured in `.pre-commit-config.yaml`; run `pre-commit run --all-files` locally before opening a PR.
- Use feature branches, include tests for new behavior, and keep changes small and focused.

---

## License 📄
This project is licensed under the terms in the `LICENSE` file.

---



