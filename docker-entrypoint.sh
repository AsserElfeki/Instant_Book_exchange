#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'admin@myproject.com', 'toor')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:80

