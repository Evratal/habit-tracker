from telegram import Update
from telegram.ext import CallbackContext
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from users.models import User
from .models import TelegramUser


def handle_message(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text

    try:
        # Проверяем, может быть это email для привязки
        validate_email(text)
        try:
            user = User.objects.get(email=text)
            tg_user, created = TelegramUser.objects.get_or_create(
                chat_id=chat_id,
                defaults={
                    'user': user,
                    'username': update.effective_user.username,
                    'first_name': update.effective_user.first_name,
                    'last_name': update.effective_user.last_name,
                }
            )
            if not created:
                tg_user.user = user
                tg_user.save()

            update.message.reply_text(
                f"Аккаунт успешно привязан к {user.email}!\n"
                "Теперь вы будете получать уведомления о привычках."
            )
        except User.DoesNotExist:
            update.message.reply_text(
                "Пользователь с таким email не найден. "
                "Пожалуйста, проверьте правильность ввода."
            )
    except ValidationError:
        # Это не email, обрабатываем как обычное сообщение
        update.message.reply_text(
            "Я не понимаю ваше сообщение. Используйте /help для списка команд."
        )
