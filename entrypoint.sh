#!/bin/sh

run_dev() {
  ./wait-for redis:6379 -t 30 && \
  ./wait-for mysql_db:3306 -t 30 && \
  python manage.py migrate && \
	python manage.py runserver 0.0.0.0:8000
}

run_celery() {
  ./wait-for redis:6379 -t 30 && \
  ./wait-for mysql_db:3306 -t 30 && \
  celery -A books.celery worker -l info
}

run() {
    python manage.py runserver 0.0.0.0:8000
}

$1
