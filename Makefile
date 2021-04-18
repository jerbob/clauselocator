test:
	cd src && \
	DJANGO_SETTINGS_MODULE='core.settings' \
	DATABASE_URL='sqlite://:memory:' \
	coverage run -m pytest

lint:
	flake8 --ignore=src && \
	isort --check-only src && \
	mypy src
