from celery import shared_task
from django.conf import settings
from telegram import Bot
from habits.models import Habit


@shared_task
def send_habit_reminder(habit_id):
    habit = Habit.objects.get(id=habit_id)
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    message = (
        f"⏰ Напоминание о привычке!\n\n"
        f"Действие: {habit.action}\n"
        f"Место: {habit.place}\n"
        f"Время на выполнение: {habit.duration} секунд\n"
    )

    if habit.reward:
        message += f"Вознаграждение: {habit.reward}\n"

    for user in habit.user.telegram.all():
        try:
            bot.send_message(
                chat_id=user.chat_id,
                text=message
            )
        except Exception as e:
            print(f"Ошибка отправки сообщения пользователю {user.chat_id}: {e}")
