.PHONY: up down logs test tests clean

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

tests:
	pytest --cov=app/ --color=yes --cov-report=term-missing  --cov-report=html --disable-pytest-warnings
clean:
	rm -rf .pytest_cache .coverage htmlcov
	find . -type d -name "__pycache__" -exec rm -r {} +
