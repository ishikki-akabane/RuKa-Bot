from RUKA import dp, OWNER_ID
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode

from RUKA.modules.disable import DisableCommandHandler
import aiofiles

#pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


@capture_error
async def ishikki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user_id = update.effective_user.id
    bot = context.bot
    await message.reply_text("I'm Alive")
    await bot.send_message(OWNER_ID, text=f"hello, {user_id}")


dp.add_handler(DisableCommandHandler(["ishikki", "ishu"], ishikki))