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
            func_name = func.__name__
            file_path = func.__code__.co_filename
            error_line = func.__code__.co_firstlineno
            
            error_message = (
                f"__Error in function **'{func_name}'**:__\n"
                f"**File:** {file_path}\n"
                f"**Line:** {error_line}\n"
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
