
from functools import wraps
from .. import CONFIG


DISABLED_CMDS = {-1002147626641: ["start"]}


def ignoreDisabled(msg: bool = False):
    """
    Ignores commands disabled in this chat.
    Uses CONFIG.DISABLED_CMDS = {chat_id: [cmd1, cmd2, ...]}
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            chat_id = message.chat.id
            cmd = message.command[0].lower() if message.command else None
            disabled = DISABLED_CMDS.get(chat_id, [])
            print(cmd, " -- ", disabled)
            if cmd in disabled:
                if msg:
                    await message.reply_text("❌ This command is disabled in this chat.")
                return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
