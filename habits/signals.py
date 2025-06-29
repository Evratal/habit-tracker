from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Habit
from datetime import datetime


@receiver(pre_save, sender=Habit)
def habit_pre_save(sender, instance, **kwargs):
    """Проверка времени выполнения привычки перед сохранением"""
    if instance.time:
        # Проверяем, что время указано в будущем
        now = datetime.now().time()
        if instance.time < now:
            # Если время уже прошло сегодня, планируем на завтра
            pass  # Здесь можно добавить логику переноса
