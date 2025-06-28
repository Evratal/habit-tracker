import os

from django.apps import AppConfig


class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self):
        # Запускаем бота при старте Django (только для production)
        if not os.getenv('RUN_MAIN') == 'true':  # Чтобы не запускалось дважды в dev-режиме
            from .bot import setup_bot
            setup_bot()
