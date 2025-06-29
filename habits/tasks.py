from celery import shared_task
from telegram import Bot
from asgiref.sync import sync_to_async

from config import settings
from habits.models import Habit


@shared_task
async def send_telegram_reminder(habit_id):
    bot = Bot(settings.TELEGRAM_BOT_TOKEN)
    habit = await sync_to_async(Habit.objects.get)(id=habit_id)

    message = (
        f"⏰ Напоминание о привычке!\n\n"
        f"Действие: {habit.action}\n"
        f"Место: {habit.place}\n"
        f"Время: {habit.time}\n"
    )

    for user in await sync_to_async(list)(habit.user.telegram.all()):
        try:
            await bot.send_message(
                chat_id=user.chat_id,
                text=message
            )
        except Exception as e:
            print(f"Ошибка отправки: {e}")
