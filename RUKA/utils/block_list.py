

from functools import wraps
from .. import CONFIG


BLOCK_LIST = [6335690010]


def BlockList(msg: bool = False):
    """
    Blocks users inside BLOCK_LIST from using the command.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            user_id = message.from_user.id
            if user_id in BLOCK_LIST:
                if msg:
                    await message.reply_text("❌ You are blocked from using this bot.")
                return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
