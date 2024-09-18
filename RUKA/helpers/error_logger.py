# error logging decorator

import traceback
import requests
from RUKA import TOKEN, ERROR_LOG_CHANNEL


def ErrorLogger(func):
    async def wrapper(client, message):
        try:
            await func(client, message)
        except Exception as e:
            # Capture the error details
            error_message = (
                f"**Error in function '{func.__name__}':**\n"
                f"**File:** {func.__code__.co_filename}\n"
                f"**Line:** {func.__code__.co_firstlineno}\n"
                f"**Error:** {str(e)}\n"
                f"**Traceback:**\n```python\n{traceback.format_exc()}```"
            )
            await message.reply_text(
                "`oppss!! Something went wrong!\nPleasw try again later :(`"
            )
            requests.get(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ERROR_LOG_CHANNEL}&text={error_message}&parse_mode=Markdown"
            )
            
    return wrapper
