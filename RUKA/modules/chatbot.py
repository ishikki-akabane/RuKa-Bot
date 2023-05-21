from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest


from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode


BOT_NAME = "Ruka"

"""
credits goes to Safone(t.me/asmsafone)
For original api safone API
"""

@capture_error
async def chatbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    text = message.text
    bot = context.bot
    user_id = update.effective_user.id
    
    reply = message.reply_to_message
    target_id = reply.from_user.id
    if text is not None:
        await bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

        url = BLUE_URL + "/chatbot"
        data = {"param": {"query": text, "user_id": user_id, "bot_name": BOT_NAME}}

        query = await bluerequest(url, data=data)
        msg = query["msg"]
            
        await message.reply_text(f"`{msg}`", parse_mode=ParseMode.MARKDOWN)



dp.add_handler(MessageHandler(filters.REPLY, chatbot, block=False))