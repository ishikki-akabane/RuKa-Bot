

from functools import wraps
from pyrogram.enums import ChatType


def privateOnly(msg: bool = False):
    """Allow execution only in private messages."""
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            if message.chat.type != ChatType.PRIVATE:
                if msg:
                    await message.reply_text("❌ This command can only be used in private chat.")
                return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
