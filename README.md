# Проект на Django с Docker, PostgreSQL и Nginx для ARRFR.

Этот репозиторий содержит Django-веб-приложение, настроенное для работы в Docker-контейнерах с PostgreSQL в качестве базы данных и Nginx в качестве веб-сервера.

Цель Проекта: Создать веб-приложение на Django для централизованного учета информации о участниках финансового рынка. Веб-приложение должно включать в себя как фронтенд, так и бэкенд, а также должно быть развернуто с использованием Docker, включая базу данных postgres и Nginx.
## Предварительные требования

Убедитесь, что у вас установлены Docker и Docker Compose на вашем компьютере.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Начало работы

1. Склонируйте этот репозиторий:

    ```bash
    git clone https://github.com/tab1k/ARRFR.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd /ARRFR
    ```

3. База данных:

    ```python
    DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    "default": {
            "ENGINE": "django.db.backends.postgresql",
            'NAME': os.getenv('DB_NAME', 'arrfr_db'),
            'USER': os.getenv('DB_USER', 'arrfr'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'TOBI8585'),
            'HOST': os.getenv('DB_HOST', 'db'),
            'PORT': os.getenv('DB_PORT', 5432),
    }
   }


    ```

4. Создайте и запустите контейнеры Docker:

    ```bash
    docker-compose up -d
    ```

5. Примените миграцию и создайте суперпользователя:

    ```bash
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    ```

6. Загрузите фикстуры (если нужно):

    ```bash
    docker-compose run web python manage.py loaddata fixtures/initial_data.json
    ```

7. Вот вы и в Django проекте.


## Дополнительная информация

- Приложение Django работает на порту 8000, а Nginx настроен для обслуживания приложения на порту 80.
- Статические файлы обслуживаются Nginx, и доступ к ним можно получить по адресу [http://localhost/static/](http://localhost/static/).
- Медиа-файлы также обслуживаются Nginx, и доступ к ним можно получить по адресу [http://localhost/media/](http://localhost/media/).

Если у вас возникнут какие-либо проблемы или возникнут вопросы, вы можете обратиться ко мне по instagram: @tab1k.k.
