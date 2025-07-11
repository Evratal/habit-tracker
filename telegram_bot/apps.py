import os

from django.apps import AppConfig


class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram_bot'

    def ready(self):
        # Запускаем бота при старте Django (только для production)
        if not os.environ.get('RUN_MAIN') and not os.environ.get('TESTING'):
            from .bot import setup_bot
            setup_bot()
