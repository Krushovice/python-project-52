#!/usr/bin/env bash
# exit on error
set -o errexit
python3 -m pip install --upgrade pip
poetry install

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
