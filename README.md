# Habit Tracker

Django-приложение для трекинга привычек по методологии Джеймса Клира ("Атомные привычки")

## Особенности

- Трекер полезных привычек
- Напоминания через Telegram
- Интеграция с Celery для отложенных задач
- REST API с JWT аутентификацией

## Демо

Приложение находится на сервере по следующему ip: 158.160.173.39


## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/evrat/habit-tracker.git
```

2. Создайте файл .env на основе .env.sample:
```bash
cp .env.sample .env
```

3. Запустите сервисы:
```bash
docker-compose up -d --build
```
4. Применение миграций:
```bash
docker-compose exec web python manage.py migrate
```

5. Создание суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Настройка сервера

- Трекер полезных привычек
- Напоминания через Telegram
- Интеграция с Celery для отложенных задач
- REST API с JWT аутентификацией

1. Установите Docker и Docker Compose на сервер

2. Скопируйте файлы проекта на сервер

3. Настройте .env файл с production значениями

4. Запустите:
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

## Требуемые secrets:

DOCKER_HUB_USERNAME - Логин Docker Hub
DOCKER_HUB_ACCESS_TOKEN - Токен Docker Hub
SSH_KEY - Приватный SSH ключ для доступа к серверу
SERVER_IP - IP адрес сервера
SSH_USER - SSH пользователь

## Технический стек:

Django 4.2
PostgreSQL 13
Redis 6
Celery 5.3
Gunicorn 20.1
Nginx
Docker