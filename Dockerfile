FROM python:3.11 as base

# Копируем все из текущей дериктории в дерикторю srv внутри docker.
COPY . /srv
# Устанавливаем рабочую дерикторию из которой
# будет осуществлятся последующее выполнение команд.
WORKDIR /srv


# Python не будет создавать файлы .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Python будет использовать не буферизованный вывод (без кэширования)
ENV PYTHONUNBUFFERED 1

# -y согласие на любые запросы на подтверждение
# -yy тоже самое, но более агрессивно, пропуская несовместимости и т.п.
# -q quite меньше информации в консоли

RUN apt-get update # Обновление списка пакетов внутри контейнера
RUN apt-get install -y dos2unix # Установка пакета dos2unix, для перевода строк в unix
RUN apt-get install -y libpq-dev # Установка пакета libpq-dev, необходимого для работы с PostgreSQL
RUN apt-get install -y netcat-openbsd # Установка netcat-openbsd, утилиты для работы с сетевыми соединениями
RUN python -m pip install --upgrade pip # Обновление инструмента pip до последней версии
RUN python -m pip install -r /srv/requirements.txt # Установка зависимостей, перечисленных в файле requirements.txt

RUN dos2unix /srv/entrypoint.dev.sh  # перевод строк в unix
RUN dos2unix /srv/entrypoint.prod.sh  # перевод строк в unix
RUN apt-get --purge remove -y dos2unix  # удаляем d2u за ненадобностью


###########
#   DEV   #
###########
FROM base as dev
RUN chmod +x /srv/entrypoint.dev.sh
ENTRYPOINT ["/srv/entrypoint.dev.sh"]

############
#   PROD   #
############
FROM base as prod
RUN chmod +x /srv/entrypoint.prod.sh
ENTRYPOINT ["/srv/entrypoint.prod.sh"]


# TODO: Убрать нахер комментарии.


