import traceback
from functools import wraps
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

from RUKA.helpers.paste_help import paste
from RUKA import ERROR_LOGS


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with aiosession.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False


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
            preview = f"{link}/preview.png"

            if await isPreviewUp(preview):
                try:
                    await bot.send_photo(
                        chat_id=chat_id,
                        photo=preview,
                        caption=error_message,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="Check", url=link)
                                ]
                            ]
                        )
                    )
                    return
                except Exception:
                    pass

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
