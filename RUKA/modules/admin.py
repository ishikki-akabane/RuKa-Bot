from RUKA import dp
from RUKA.helpers.rank_help import status

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


BAN_STICKER = ""

@status(rank="support")
async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    bot = context.bot
    args = context.args
    reply = message.reply_to_message

    if reply:
        target_id = reply.from_user.id
    elif len(args) == 0:
        return await message.reply_text("Babe :)\ngive me something to ban")
    else:
        try:
            target_id = args[0]
            target_id = int(target_id)
        except:
            return await message.reply_text("Sorry, i cant find that user")

    try:
        await chat.ban_member(target_id)
        await bot.send_sticker(chat.id, BAN_STICKER)
        await message.reply_text("I successfully banned that user!")
    except:
        return await message.reply_text("opps!! something went wrong")


@status(rank="support")
async def unban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    bot = context.bot
    args = context.args
    reply = message.reply_to_message

    if reply:
        target_id = reply.from_user.id
    elif len(args) == 0:
        return await message.reply_text("Love Day :)\ngive me something to unban")
    else:
        try:
            target_id = args[0]
            target_id = int(target_id)
        except:
            return await message.reply_text("Sorry, i cant find that user")
    
    try:
        await chat.unban_member(target_id)
        await message.reply_text("I successfully unbanned that user :)")
    except:
        return await message.reply_text("opps!! something went wrong")


@status(rank="support")
async def kick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    bot = context.bot
    args = context.args
    reply = message.reply_to_message

    if reply:
        target_id = reply.from_user.id
    elif len(args) == 0:
        return await message.reply_text("Love Day :)\ngive me something to kick")
    else:
        try:
            target_id = args[0]
            target_id = int(target_id)
        except:
            return await message.reply_text("Sorry, i cant find that user")
    
    try:
        await chat.unban_member(target_id)
        await message.reply_text("I successfully kicked his ass out of the group :)")
    except:
        return await message.reply_text("opps!! something went wrong")


@status(rank="support")
async def delete_replied_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the replied message
    replied_message = update.message.reply_to_message
    
    if replied_message:
        # Delete the replied message
        await replied_message.delete()
        await update.message.reply_text("Message vanished!! :)")
    else:
        # Handle the case when there is no replied message
        await update.message.reply_text('No replied message found :)')




dp.add_handler(CommandHandler("ban", ban, block=False))
dp.add_handler(CommandHandler("unban", unban, block=False))
dp.add_handler(CommandHandler("kick", kick, block=False))
dp.add_handler(CommandHandler("del", delete_replied_message, block=False))