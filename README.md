# Django Docker Template

Этот проект представляет собой шаблон для быстрого старта 
веб-приложений на базе Django, с использованием контейнеризации 
Docker и интеграцией таких инструментов, как: <br><br>
`Django` `PostgreSQL` `Nginx` `Gunicorn` `Redis`

- Готовая конфигурация Docker для dev и prod.
- Настроенный Nginx как reverse proxy к Gunicorn.
- Встроенная поддержка PostgreSQL и Redis.
- Подробные комментарии. 
- Поддержка MediaFiles

## Использование

1. ### Клонируйте репозиторий
   ```git
   git clone https://github.com/Artasov/django-docker-template.git
   cd django-docker-template
   ```
2. ### Запустите Docker Compose
   * #### Development
     ```docker
     docker-compose --env-file .env.dev -f docker-compose.dev.yml up -d --build
     ```
   * #### Production
     ```docker
     docker-compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
     ```
3. ### Django-приложение доступно по адресу [http://localhost:8000](http://localhost:8000)<br><br><br>

## Другое


>Если у вас есть предложения по улучшению проекта или вы обнаружили ошибку, 
пожалуйста, создайте issue или отправьте Pull Request.
