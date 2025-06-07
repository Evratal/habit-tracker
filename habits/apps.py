from django.apps import AppConfig


class HabitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'habits'

    # Полностью отключаем ready() на время миграций
    # def ready(self):
    #     import habits.signals