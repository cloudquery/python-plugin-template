test:
	poetry run pytest . -vv

fmt:
	poetry run black .

fmt-check:
	poetry run black --check .
