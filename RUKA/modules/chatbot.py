from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest
from RUKA.database.sql.chatbot_sql import sql_addchatbot, sql_removechatbot, sql_updatechatbot, checkchat

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode


BOT_NAME = "Ruka"


async def chatbot1(text, user_id):
    url = BLUE_URL + "/chatbot1"
    data = {"param": {"query": text, "user_id": user_id, "bot_name": BOT_NAME}}
    query = await bluerequest(url, data=data)
    msg = query["msg"]
    return msg


async def chatbot2(text):
    url = BLUE_URL + "/chatbot2"
    data = {"param": {"query": text, "bot_name": BOT_NAME}}
    query = await bluerequest(url, data=data)
    msg = query["msg"]
    return msg



@capture_error
async def chatbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat_id = update.effective_chat.id
    version = await checkchat(chat_id)
    text = message.text
    bot = context.bot
    
    reply = message.reply_to_message
    target_id = reply.from_user.id
    if target_id == 6208314828:
        if version == 1:
            await bot.send_chat_action(chat_id=chat_id, action='typing')
            user_id = update.effective_user.id
            if text is not None:
                msg = await chatbot1(text, user_id)
                await message.reply_text(f"{msg}", parse_mode=ParseMode.MARKDOWN)

        elif version == 2:
            await bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
            if text is not None:
                msg = await chatbot2(text)
                await message.reply_text(f"{msg}", parse_mode=ParseMode.MARKDOWN)

        else:
            return
    
        



dp.add_handler(MessageHandler(filters.REPLY, chatbot, block=False))
