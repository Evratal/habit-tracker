import os
from telegram import Bot, Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    Updater,
    CallbackContext
)
from django.conf import settings

from telegram_bot.models import TelegramUser
from users.models import User

bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))


def start(update: Update, context: CallbackContext):
    """Обработка команды /start"""
    email = update.message.text.split()[1] if len(update.message.text.split()) > 1 else None

    if email:
        try:
            user = User.objects.get(email=email)
            TelegramUser.objects.update_or_create(
                user=user,
                defaults={'chat_id': update.message.chat_id}
            )
            update.message.reply_text("✅ Вы успешно привязали аккаунт!")
        except User.DoesNotExist:
            update.message.reply_text("❌ Пользователь не найден")
    else:
        update.message.reply_text("Отправьте команду в формате: /start ваш_email@example.com")


def setup_dispatcher(dp):
    """Регистрация обработчиков команд"""
    dp.add_handler(CommandHandler("start", start))
    return dp