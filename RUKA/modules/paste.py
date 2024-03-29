import asyncio
import os
import re
import aiofiles


from RUKA import dp, aiosession
from RUKA.helpers.errors import capture_error
from RUKA.helpers.paste_help import paste

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputFile  
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with aiosession.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False



async def paste_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    bot = context.bot
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ `/paste`", parse_mode=ParseMode.MARKDOWN)

    await message.reply_text("ᴘᴀsᴛɪɴɢ...")
    if reply.text:
        content = str(reply.text)
    elif reply.document:
        document = reply.document
        if document.file_size > 1048576:
            return await message.reply_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴘᴀsᴛᴇ ғɪʟᴇs sᴍᴀʟʟᴇʀ ᴛʜᴀɴ 1ᴍʙ.")
        if not pattern.search(document.mime_type):
            return await message.reply_text("ᴏɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.")

        file_id = document.file_id
        # Get the file object using the file_id
        file = await bot.get_file(file_id)
        doc = await file.download_to_drive()
        
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    else:
        return await message.reply_text("not supported!")

    link = await paste(content)
    preview = f"{link}/preview.png"

    if await isPreviewUp(preview):
        try:
            await message.reply_photo(
                photo=preview,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Your paste link", url=link)
                        ]
                    ]
                )
            )
            return
        except Exception:
            pass

    await message.reply_text(
        text="Your file is pasted on ezup.dev!\nBy: @Ishikki",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Your paste link", url=link)
                ]
            ]
        )
    )



dp.add_handler(CommandHandler("paste", paste_func, block=False))
