import os
import json
import requests
import aiohttp
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler

from RUKA import dp

api_key = "blue-api-testing"
url = 'https://blue-api.vercel.app/reverse'


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
        print(file_path)
        file_obj = await context.bot.get_file(file_id)
        print(file_obj)
        file_url = file_obj.file_path
        print(file_url)

    else:
        await message.reply_text(
            "Please Reply To A Sticker, Or An Image To Search It!"
        )
        return

    try:
        data = {"img_url": file_url}
        headers = {"API-KEY": api_key}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as resp:
                    response_text = await resp.json()

            await message.reply_text(
                text=response_text["reverse"],
                reply_markup=InlineKeyboardMarkup(
                    [
                        InlineKeyboardButton(text="Link", url=response_text["url"])
                    ]
                )
            )
        except:
            await message.reply_text("Cant find anything!!")
    except Exception as e:
        print(e)


dp.add_handler(CommandHandler(["pp", "grs", "p", "reverse"], reverse))