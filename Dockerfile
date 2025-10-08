FROM ghcr.io/astral-sh/uv:python3.13-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --no-install-project

ENV PATH="/app/.venv/bin:${PATH}"

COPY . .

CMD ["bash", "-lc", "uv run uvicorn app.main:app --host 0.0.0.0 --port 8000"]
