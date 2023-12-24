install:
	./build.sh

start:
	gunicorn task_manager.wsgi:application

shell:
	poetry run python manage.py shell

lint:
	poetry run flake8 task_manager/ --exclude=migrations

test:
	poetry run coverage run --source='.' manage.py test

test-coverage:
	poetry run coverage xml
