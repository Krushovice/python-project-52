#!/usr/bin/env bash
# exit on error
set -o errexit
python3 -m pip install --upgrade pip
python3 -m install poetry==1.7.0
rm poetry.lock
poetry lock
poetry install

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
