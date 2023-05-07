from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from RUKA.helpers import DEVLIST, SUDOLIST, SUPPORTLIST, WHITELIST, OWNER_ID, LOGGER


def status(rank):
    def decorator(func):
        @wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
            user_id = update.effective_user.id
            message = update.effective_message

            if rank == 'dev' and user_id not in DEVLIST:
                await message.reply_text("Only developers of the bot can use this command")
                return
            elif rank == 'sudo' and user_id not in SUDOLIST:
                await message.reply_text("Only user with sudo access can use this command")
                return
            elif rank == 'support' and user_id not in SUPPORTLIST:
                await message.reply_text("You not worthy to use this command")
                return
            elif rank == 'white' and user_id not in WHITELIST:
                await message.reply_text("Only for special ranks user!!")
                return
            elif rank == 'owner' and user_id != OWNER_ID:
                await message.reply_text("Only my dear owner can you use this!!")
                return

            return await func(update, context)
        return wrapper
    return decorator
