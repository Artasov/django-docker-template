FROM python:3.11-alpine as base

# Copy everything from the current directory to the srv directory inside docker
COPY . /srv
# Set the working directory from which
# subsequent execution of commands will be carried out
WORKDIR /srv

# Python will not create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Python will use unbuffered output (no caching)
ENV PYTHONUNBUFFERED 1



# -y agree to any confirmation requests
# -yy is the same thing, but more aggressive, skipping incompatibilities, etc.
# -q quite less information in the console

RUN apt-get update # Update the list of packages inside the container
RUN apt-get install -y dos2unix # Install the dos2unix package, to translate strings to unix
RUN apt-get install -y libpq-dev # Install the libpq-dev package required to work with PostgreSQL
RUN apt-get install -y netcat-openbsd # Install netcat-openbsd, a utility for working with network connections
RUN python -m venv /venv # Create and activate a virtual environment
ENV PATH="/venv/bin:$PATH"
RUN python -m pip install --upgrade pip # Upgrade the pip tool to the latest version
RUN python -m pip install -r /srv/requirements.txt # Install the dependencies listed in requirements.txt
RUN dos2unix /srv/entrypoint.prod.sh # translate strings to unix
RUN apt-get --purge remove -y dos2unix # remove d2u as unnecessary
RUN chmod +x /srv/entrypoint.prod.sh
RUN touch /srv/celerybeat-schedule && chmod 666 /srv/celerybeat-schedule # For celerybeat

RUN mkdir -p /srv/logs
RUN touch /srv/logs/access.log /srv/logs/error.log
RUN chmod 666 /srv/logs/access.log /srv/logs/error.log
USER base_user

RUN useradd -ms /bin/bash base_user
RUN chown -R base_user:base_user /srv/logs

# Create a user without administrator rights and switch to it.


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