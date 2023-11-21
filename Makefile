install:
	./build.sh

start:
	gunicorn task_manager.wsgi:application

shell:
	poetry run python manage.py shell
