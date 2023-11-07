install:
	./build.sh

start:
	gunicorn mysite.wsgi:application
