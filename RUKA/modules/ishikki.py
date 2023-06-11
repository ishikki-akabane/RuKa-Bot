from RUKA import dp, OWNER_ID
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode

from RUKA.modules.disable import DisableCommandHandler
import re

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

@capture_error
async def ishikki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user_id = update.effective_user.id
    bot = context.bot
    await message.reply_text("I'm Alive")
    await bot.send_message(OWNER_ID, text=f"hello, {user_id}")


async def abcfunc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    bot = context.bot
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ `/paste`", parse_mode=ParseMode.MARKDOWN)

    msg = await message.reply_text("ᴘᴀsᴛɪɴɢ...")
    if reply.text:
        content = str(reply.text)
    elif reply.document:
        document = reply.document
        if document.file_size > 1048576:
            return await msg.edit_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴘᴀsᴛᴇ ғɪʟᴇs sᴍᴀʟʟᴇʀ ᴛʜᴀɴ 1ᴍʙ.")
        if not pattern.search(document.mime_type):
            return await msg.edit_text("ᴏɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.")

        file_id = document.file_id
        # Get the file object using the file_id
        file = await bot.get_file(file_id)
        print(file)
        #doc = await bot.download_file(document.file_id)
        #doc = doc_file.download()
        doc = file.file_path
        print(doc)

        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
            
    else:
        return await message.reply_text("lol")
    
    await message.reply_text(content)

dp.add_handler(CommandHandler("abc", abcfunc))
dp.add_handler(DisableCommandHandler(["ishikki", "ishu"], ishikki))
