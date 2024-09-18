from pyrogram import Client, filters
from RUKA.helpers.error_logger import ErrorLogger


#@ErrorLogger
@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("started...") #, haha="haha")
