
from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest
from RUKA.helpers.rank_help import status
from RUKA.database.sql.chatbot_sql import sql_addchatbot, sql_removechatbot, sql_updatechatbot, checkchat, chatbot_list

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
    else:
        if len(args) > 0:
            try:
                target_id = args[0]
                target_id = int(target_id)
                target = await bot.get_chat(target_id)
                await message.reply_text(f"{target.first_name}")
            except Exception as e:
                print(e)
                if args[0][0] == "@":
                    user_name = args[0]
                    target_id = await get_user_id(user_name)
                    await message.reply_text(f"{target_id}")
                return await message.reply_text("User id is not valid!!")
        else:
            return await message.reply_text("Bro wtf, you havent provided me anything :/")

        
dp.add_handler(CommandHandler("infoo", info, block=False))