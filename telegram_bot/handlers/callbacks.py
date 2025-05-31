from telegram import Update
from telegram.ext import CallbackContext


def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    # Обработка разных callback_data
    if data.startswith('habit_'):
        habit_id = data.split('_')[1]
        # Логика обработки привычки
        query.answer(f"Привычка {habit_id} выполнена!")
        query.edit_message_text(text=f"✅ Привычка {habit_id} отмечена как выполненная")