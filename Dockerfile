FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.11.2 /uv /uvx /bin/

WORKDIR /app

# Copy dependency files and install
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --no-install-project

# Copy the rest of the code
COPY plugin plugin
COPY main.py .
RUN uv sync --frozen --no-dev

EXPOSE 7777

ENTRYPOINT ["uv", "run", "main"]

CMD ["serve", "--address", "[::]:7777", "--log-format", "json", "--log-level", "info"]
