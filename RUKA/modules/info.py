
from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest
from RUKA.helpers.rank_help import status
from RUKA.database.sql.user_sql import sql_get_userid

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode


@capture_error
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.effective_message
    chat_id = update.effective_chat.id
    args = context.args
    bot = context.bot

    reply = message.reply_to_message
    if reply:
        target = reply.from_user
        target_id = target.id
    else:
        if len(args) > 0:
            if args[0][0] == "@":
                user_name = args[0]
                user_name = user_name[1:]
                try:
                    target_id = await sql_get_userid(user_name)
                except:
                    return await message.reply_text("User not found :(")
            else:
                try:
                    target_id = args[0]
                    target_id = int(target_id)
                except:
                    return await message.reply_text("User id is not valid!!")

            try:
                target = await bot.get_chat(target_id)
            except:
                return await message.reply_text("User not found :(")        
        else:
            return await message.reply_text("Bro wtf, you havent provided me anything :/")
    
    first_name =  target.first_name
    if target.last_name:
        last_name = target.last_name
    else:
        last_name = None
    user_name = target.username
    info_msg = f"""
---------------
userID: {target_id}
firstname: {first_name}
lastname: {last_name}
username: {username}
---------------
"""
    await message.reply_text(
        info_msg,
        parse_mode=ParseMode.MARKDOWN
    )

        
dp.add_handler(CommandHandler("infoo", info, block=False))