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
                f"Error in function <b>'{func_name}'</b>:\n"
                f"<b>File:</b> {file_path}\n"
                f"<b>Line:</b> {error_line}\n"
                f"<b>Error:</b> {str(e)}\n"
                f"<b>Traceback:</b>\n<code lang='python'>{traceback.format_exc()}</code>"
            )
            await message.reply_text(
                "`oppss!! Something went wrong!\nPleasw try again later :(`"
            )
            requests.get(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ERROR_LOG_CHANNEL}&text={error_message}&parse_mode=HTML"
            )
            
    return wrapper
