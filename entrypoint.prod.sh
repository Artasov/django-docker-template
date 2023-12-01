#!/bin/sh

############
#   PROD   #
############
echo "Start PROD mode"

if [ "$SQL_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    # Пока не установлено соединение с PostgreSQL, ждем
    while ! nc -z postgres "$SQL_PORT"; do
      sleep 0.1
    done
    echo "Postgres started"
fi

# Собираем статические файлы в одну папку без запроса подтверждения
python manage.py collectstatic --noinput &&
# Создаем файлы миграций
#python manage.py makemigrations &&
# Применяем миграции к базе данных
python manage.py migrate &&
# Биндим gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000

# TODO: Стереть комментарии