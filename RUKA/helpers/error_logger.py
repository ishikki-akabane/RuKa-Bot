# error logging decorator

import traceback
import requests
from RUKA import TOKEN, ERROR_LOG_CHANNEL
from RUKA.database import db


def ErrorLogger(func):
    async def wrapper(client, message):
        try:
            await func(client, message)
        except Exception as e:
            # Capture the error details
            chat_id = message.from_user.id
            func_name = func.__name__
            file_path = func.__code__.co_filename
            error_line = func.__code__.co_firstlineno
            
            error_message = (
                f"Error in function <b>'{func_name}'</b>:\n"
                f"<b>File:</b> {file_path}\n"
                f"<b>Line:</b> {error_line}\n"
                f"<b>Error:</b> {str(e)}\n"
                f"<b>Traceback:</b>\n<pre language='python'>{traceback.format_exc()}</pre>"
            )
            await message.reply_text(
                "`oops!! Something went wrong!\nPlease try again later :(`"
            )
            requests.get(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ERROR_LOG_CHANNEL}&text={error_message}&parse_mode=HTML"
            )
            await db.add_error(chat_id, func_name, file_path, error_line, e)
            
    return wrapper
