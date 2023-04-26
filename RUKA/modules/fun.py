import json
import aiohttp

from RUKA import dp, BLUE_API
from RUKA.helpers.extra import mention

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


baseblue_url = "https://blue-api.vercel.app"


async def slap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = (
        message.reply_to_message.reply_text
        if message.reply_to_message
        else message.reply_text
    )

    reply = message.reply_to_message
    if not reply:
        await message.reply_text("can i slap you please :)")
        return

    attacker = update.effective_user.id # user id of the user who is slapping
    defender = message.reply_to_message.from_user.id
     
    await message.reply_text(f"{attacker}   {defender}")


dp.add_handler(CommandHandler("slap", slap))