test:
	cd src && \
	DJANGO_SETTINGS_MODULE='core.settings' \
	DATABASE_URL='sqlite://:memory:' \
	pytest --cov=. --cov-report=xml

lint:
	flake8 --ignore=src && \
	isort --check-only src && \
	mypy src

build:
	docker build -t ghcr.io/jerbob/clauselocator . && \
	docker build -t ghcr.io/jerbob/caddy caddy

deploy-live:
	docker push ghcr.io/jerbob/clauselocator && \
	docker push ghcr.io/jerbob/caddy
