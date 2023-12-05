#!/bin/bash
set -e

# Ждем, пока база данных PostgreSQL станет доступной
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DB_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

# Выполняем миграции Django
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
python manage.py runserver 0.0.0.0:8000

# Запускаем Django-приложение
exec "$@"

