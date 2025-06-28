from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для трекинга привычек.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Помощь по использованию бота...")


def setup_bot():
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    if settings.DEBUG:
        application.run_polling()
    else:
        application.run_webhook(
            listen="0.0.0.0",
            port=8000,
            webhook_url=f"https://{settings.ALLOWED_HOSTS[0]}/api/telegram/webhook/"
        )
