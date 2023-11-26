install:
	./build.sh

start:
	gunicorn task_manager.wsgi:application

migrate:
	poetry run python manage.py makemigrations & poetry run python manage.py migrate

shell:
	poetry run python manage.py shell
