#!/bin/bash

# Текущая дата
current_date=$(date +%F)

# Директория логов
log_directory="./logs"

# Создание директории
mkdir -p $log_directory

# Имя файла лога
log_file="${log_directory}/project_container_${current_date}.log"

# Запуск docker-compose в фоновом режиме
docker-compose --env-file .env.prod -f docker-compose.prod.yml up -d --build

# Запись логов в файл
docker-compose logs -f >> "$log_file" 2>&1