from pyrogram import Client, filters
from RUKA.helpers.error_logger import ErrorLogger


@Client.on_message(filters.command("start"))
@ErrorLogger
async def start_cmd(client, message):
    await message.reply_text("started...", haha="haha")
