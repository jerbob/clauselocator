test:
	cd src && \
	DJANGO_SETTINGS_MODULE='core.settings' \
	DATABASE_URL='sqlite://:memory:' \
	pytest --cov=.

lint:
	flake8 --ignore=src && \
	isort --check-only src && \
	mypy src
