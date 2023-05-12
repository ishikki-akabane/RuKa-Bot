from RUKA import dp, OWNER_ID
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode

@capture_error
async def ishikki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    bot = context.bot
    await message.reply_text("I'm Alive")
    await bot.send_message(OWNER_ID, bot)


dp.add_handler(CommandHandler("ishikki", ishikki))