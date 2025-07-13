# Базовый образ Python
FROM python:3.10

# Установка системных зависимостей
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Оптимизация: сначала копируем только requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Копирование всего проекта (с учетом .dockerignore)
COPY . .

# Создание директорий для статики и медиа
RUN mkdir -p /app/staticfiles /app/media \
    && chown -R 1000:1000 /app/staticfiles /app/media \
    && chmod -R 755 /app/staticfiles /app/media

# Запуск миграций и сборки статики (опционально)
RUN if [ "$COLLECTSTATIC" = "true" ]; then python manage.py collectstatic --noinput; fi

# Пользователь для безопасности
USER 1000

# Порт и команда запуска
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

