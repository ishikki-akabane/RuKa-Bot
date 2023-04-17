from RUKA import dp

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


async def ishikki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    await message.reply_text("I'm Alive")


dp.add_handler(CommandHandler("ishikki", ishikki))