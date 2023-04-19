from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from RUKA import LOGGER, dp
from RUKA.helpers.rank_help import status


@status(rank="dev")
async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    if chat.type != "private":
        await message.reply_text("I sent your logs into your dm.")
        
    with open("logs.txt", "rb") as f:
        await context.bot.send_document(document=f, filename=f.name, chat_id=user.id)


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):



dp.add_handler(CommandHandler("logs", logs, block=False))
dp.add_handler(CommandHandler("stats", stats, block=False))