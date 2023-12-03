# Django Server Docker Template

This template is for quickly starting web applications based on _Django_,
using containerization _Docker_ and integration of tools such as:<br><br>
`Docker` `Django` `Celery` `Beat Sheduler` `Flower` `Cache` `PostgreSQL` `Redis` `Minio` `Nginx` `Gunicorn`

## Start

1. ### Clone
    ```git
    git clone https://github.com/Artasov/django-docker-template.git
    mv django-docker-template project_name
    cd project_name
    ```
2. ### Запустите Docker Compose
      ```docker
      docker-compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
      ```
## Info
1. ### Endpoints
    * **django [http://localhost:8000](http://localhost:8000)**
    * **minio files [http://127.0.0.1:9000](http://127.0.0.1:9000)**
    * **minio console [http://127.0.0.1:9001](http://127.0.0.1:9001)**
    * **flower [http://127.0.0.1:5555/flower](http://127.0.0.1:5555/flower)**<br><br>
2. ### Cache
   Using `django-redis` + `django-cachalot`
3. ### Logs
   Edit `build.up.sh` and run it now.
   ```shell
   chmod +x build_up.sh
   build_up.sh
   ```
   By default, the entire `docker-compose console` will be
   logged to `logs/datatime_log_file.log`, a **new file every day**.
4. ### Other
   All settings in `.env.prod`

> If you have suggestions for improving the project or you find a bug,
> please create an issue or send a Pull Request.
