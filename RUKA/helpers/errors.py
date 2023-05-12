import traceback
from functools import wraps
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

from RUKA.helpers.paste_help import paste
from RUKA import ERROR_LOGS


def capture_error(func):
    @wraps(func)
    async def wrapper(update, context, *args, **kwargs):
        try:
            return await func(update, context, *args, **kwargs)
        except Exception as e:
            error_message = f"An error occurred: {e}\n\n"
            tracebackk = traceback.format_exc()
            error_message += f"{traceback}"
            bot = context.bot
            chat_id = ERROR_LOGS
            link = await paste(tracebackk)
            await bot.send_message(
                chat_id=chat_id,
                text=error_message,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Check", url=link)
                        ]
                    ]
                )
            )
    return wrapper
