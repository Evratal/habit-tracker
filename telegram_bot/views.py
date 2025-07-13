from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
from telegram import Update
from telegram.ext import Application, CommandHandler

from config import settings


@csrf_exempt
async def telegram_webhook(request):
    if request.method == 'POST':
        application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

        # Регистрация обработчиков
        from .handlers.commands import start, help_command
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))

        update = await sync_to_async(Update.de_json)(
            data=request.body.decode('utf-8'),
            bot=application.bot
        )
        await application.process_update(update)

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'method not allowed'}, status=405)
