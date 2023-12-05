FROM python:3.11-alpine as base

COPY . /srv
WORKDIR /srv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add dos2unix
RUN apk add libpq-dev
RUN apk add netcat-openbsd
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /srv/requirements.txt
RUN dos2unix /srv/entrypoint.prod.sh
RUN apk del dos2unix
RUN chmod +x /srv/entrypoint.prod.sh

RUN touch /srv/celerybeat-schedule && chmod 666 /srv/celerybeat-schedule
RUN touch /srv/celerybeat.pid && chmod 666 /srv/celerybeat.pid
RUN mkdir -p /srv/logs

RUN adduser -D base_user
RUN chown -R base_user:base_user /srv/logs
RUN chown base_user:base_user /srv/celerybeat.pid  # Change ownership of the PID file to base_user

USER base_user


###########
# DEV #
###########
FROM base as dev
ENTRYPOINT ["sh", "/srv/entrypoint.dev.sh"]

#############
# PROD #
#############
FROM base as prod
ENTRYPOINT ["sh", "/srv/entrypoint.prod.sh"]