test:
	uv run pytest . -vv

fmt:
	uv run black .

fmt-check:
	uv run black --check .
