# Habit Tracker

Django-приложение для трекинга привычек по методологии Джеймса Клира ("Атомные привычки")

## Особенности

- Трекер полезных привычек
- Напоминания через Telegram
- Интеграция с Celery для отложенных задач
- REST API с JWT аутентификацией

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/habit-tracker.git
```

2. Установите зависимости:
```bash
poetry install
```

3. Настройте переменные окружения (создайте `.env` файл):
```
SECRET_KEY=ваш-secret-key
DEBUG=True
TELEGRAM_BOT_TOKEN=ваш-токен
```

4. Запустите миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```