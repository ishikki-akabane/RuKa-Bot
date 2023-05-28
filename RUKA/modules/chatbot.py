from io import BytesIO

from RUKA import dp, BLUE_URL
from RUKA.helpers.errors import capture_error
from RUKA.helpers.requests import bluerequest
from RUKA.helpers.rank_help import status
from RUKA.database.sql.chatbot_sql import sql_addchatbot, sql_removechatbot, sql_updatechatbot, checkchat, chatbot_list

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode


BOT_NAME = "Ruka"


async def chatbot1(text, user_id):
    """credits goes to safone api for this wonderfull chatbot version"""
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
async def chatbot_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.effective_message
    chat_id = update.effective_chat.id
    version = await checkchat(chat_id)
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Safone", callback_data=f"chatbot=safone={chat_id}")],
            [InlineKeyboardButton(text="Kurumi", callback_data=f"chatbot=kurumi={chat_id}")],
            [InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"chatbot=disable={chat_id}")],
        ]
    )
    if version == 1:
        msg = "Your chatbot is activated!!\nchatbot: Safone\n"
    elif version == 2:
        msg = "Your chatbot is activated!!\nchatbot: Kurumi\n"
    else:
        msg = "Your chatbot is a deactivated!!\n"

    msg += f"\nWhich chatbot you want to activate?\nsafone: An advanced chatbot created by safone\nKurumi: A beta-testing chatbot(still in development)"

    await message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@capture_error
async def chatbot_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    message = update.effective_message
    commands = query.data.split("=")
    if commands[0] == "chatbot":
        chat_id = int(commands[2])
        exist = await checkchat(chat_id)
        
        if commands[1] == "safone":
            if exist == 1:
                await message.edit_text("SafOne ChatBot Activated!!\nHey buddy, how are you?")
            if exist == 2:
                result = await sql_updatechatbot(chat_id, 1)
                await message.edit_text("SafOne ChatBot Activated!!\nHey buddy, how are you?")
            else:
                result = await sql_addchatbot(chat_id, 1)
                await message.edit_text("SafOne ChatBot Activated!!\nHey buddy, how are you?")
            
        elif commands[1] == "kurumi":
            if exist == 1:
                result = await sql_updatechatbot(chat_id, 2)
                await message.edit_text("KurumiAPI ChatBot Activated!!\nHeya fellow, wassup?")
            if exist == 2:
                await message.edit_text("KurumiAPI ChatBot Activated!!\nHeya fellow, wassup?")
            else:
                result = await sql_addchatbot(chat_id, 2)
                await message.edit_text("KurumiAPI ChatBot Activated!!\nHeya fellow, wassup?")

        elif commands[1] == "disable":
            result = await sql_removechatbot(chat_id)
            await message.edit_text("Chatbot deactivated!!")

        else:
            result = None
            await query.message.edit_text("Chatbot deactivated!!")


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
   

@status(rank="dev")
@capture_error
async def chatbotlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chatbots = await chatbot_list()
    if chatbots:
        chatfile = "I'm talking with these peoples:)\n"
        chatfile += "[x] -   [Chat ID]    - [Version]\n\n"
        for chatbot in chatbots:
            if chatbot[0] > 10:
                chatfile += f"[x] -   {chatbot[0]}   - {chatbot[1]}\n"
            else:
                chatfile += f"[x] - {chatbot[0]} - {chatbot[1]}\n"
        with BytesIO(str.encode(chatfile)) as output:
            output.name = "AIchatlist.txt"
            await message.reply_document(
                document=output,
                filename="AIchatlist.txt",
                caption="currently active chatbot groups::",
            )
    else:
        await message.reply_text(text="No active chatbots sir :/")
        



dp.add_handler(MessageHandler(filters.REPLY, chatbot, block=False))
dp.add_handler(CommandHandler("chatbot", chatbot_select, block=False))
dp.add_handler(CallbackQueryHandler(chatbot_handler, block=False))
dp.add_handler(CommandHandler("chatbotstats", chatbotlist, block=False))
