import os
import json
import requests
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from RUKA import dp

api_key = "blue-api-testing"
url = 'https://blue-api.vercel.app/reverse/'


async def reverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    chat_id = update.effective_chat.id
    rtmid = message.message_id

    reply = message.reply_to_message

    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
            new_id = reply.sticker.file_unique_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
            new_id = reply.photo[-1].file_unique_id
        else:
            await message.reply_text("Reply To An Image Or Sticker To Lookup!")
            return

        file_path = os.path.join("temp", f"{new_id}.jpg")
        file_obj = await context.bot.get_file(file_id)
        file_url = file_obj.file_path

    else:
        await message.reply_text(
            "Please Reply To A Sticker, Or An Image To Search It!"
        )
        return

    try:
        params = {'api_token': api_key, 'image_url': file_url}
        response = requests.get(url, params=params)
        if response.status_code  == 200:
            await message.reply_text(response.text)
        else:
            await message.reply_text("Cant find anything!!")
            print(response.text)
    except Exception as e:
        print(e)


dp.add_handler(CommandHandler(["pp", "grs", "p", "reverse"], reverse))