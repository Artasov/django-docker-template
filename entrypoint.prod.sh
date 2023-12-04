#!/bin/sh

############
#   PROD   #
############



# Log files
mkdir -p /srv/logs
touch /srv/logs/access.log /srv/logs/error.log
chmod 666 /srv/logs/access.log /srv/logs/error.log
chown -R base_user:base_user /srv/logs


# Collect static files into one folder without asking for confirmation
python manage.py collectstatic --noinput &&
# Create migration files
#python manage.py makemigrations &&
# Apply migrations to the database
python manage.py migrate &&
# Bind gunicorn
gunicorn config.wsgi:application --workers 1 --bind 0.0.0.0:8000 --timeout 60 --max-requests 1000 --access-logfile /srv/logs/access.log --error-logfile /srv/logs/error.log

