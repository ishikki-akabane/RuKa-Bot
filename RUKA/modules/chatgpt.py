from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest


from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode


@capture_error
async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    text = message.text
    bot = context.bot
    user_id = update.effective_user.id
    
    reply = message.reply_to_message
    target_id = reply.from_user.id
    if target_id == 6208314828:
        if text is not None:
            await bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

            url = BLUE_URL + "/chatgpt"
            data = {"param": {"message": text, "chat_mode": "code_assistant"}}

            query = await bluerequest(url, data=data)
            msg = query["msg"]
            
            await message.reply_text(f"{msg}", parse_mode=ParseMode.MARKDOWN)



dp.add_handler(CommandHandler("ask", chatbot, block=False))