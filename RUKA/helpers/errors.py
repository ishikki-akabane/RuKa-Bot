import traceback
from functools import wraps
from telegram import Bot

from RUKA import ERROR_LOGS


def capture_error(func):
    @wraps(func)
    async def wrapper(update, context, *args, **kwargs):
        try:
            return await func(update, context, *args, **kwargs)
        except Exception as e:
            error_message = f"An error occurred: {e}\n\n"
            error_message += f"{traceback.format_exc()}"
            bot = context.bot
            chat_id = ERROR_LOGS
            await bot.send_message(chat_id=chat_id, text=error_message)
    return wrapper
