#!/bin/sh

############
#   PROD   #
############

#mkdir -p /srv/celerybeat-volume/
#touch /srv/celerybeat-volume/celerybeat-schedule && chmod 666 /srv/celerybeat-volume/celerybeat-schedule
#touch /srv/celerybeat-volume/celerybeat.pid  && chmod 666 /srv/celerybeat-volume/celerybeat-schedule

#source /srv/venv/bin/activate

# Collect static files into one folder without asking for confirmation
python manage.py collectstatic --noinput &&
# Apply migrations to the database
python manage.py migrate
# Bind gunicorn
gunicorn config.wsgi:application --workers 1 --bind 0.0.0.0:8000 --timeout 60 --max-requests 1000

