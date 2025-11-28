
from functools import wraps
from pyrogram.enums import ChatType


def groupOnly(msg: bool = False):
    """Allow execution only in group or supergroup chats."""
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
                if msg:
                    await message.reply_text("❌ This command can only be used in groups.")
                return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
