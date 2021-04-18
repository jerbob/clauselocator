test:
	cd src && \
	DJANGO_SETTINGS_MODULE='core.settings' \
	DATABASE_URL='sqlite://:memory:' \
	pytest --cov=. --cov-report html && \
	xdg-open htmlcov/index.html

lint:
	flake8 --ignore=src && \
	isort --check-only src && \
	mypy src
