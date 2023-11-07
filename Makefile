install:
	./build.sh

start:
	gunicorn task_manager.wsgi:application
