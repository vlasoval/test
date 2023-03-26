#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Start server
echo "Starting server"
gunicorn app_to_dockerize.wsgi:application --bind 0.0.0.0:8000 --workers 3