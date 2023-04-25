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

        a = await message.reply_text("searching...")
        file_path = os.path.join("temp", f"{new_id}.jpg")
        file_obj = await context.bot.get_file(file_id)
        file_url = file_obj.file_path


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

            result = response_text["reverse"]
            url_link = response_text["url"]
            await message.reply_text(
                text=result,
                reply_markup=InlineKeyboardMarkup(
                    [
                        InlineKeyboardButton(text="Link", url=url_link)
                    ]
                )
            )
        except:
            await message.reply_text("Cant find anything!!")
    except Exception as e:
        print(e)
    
    await a.delete()


dp.add_handler(CommandHandler(["pp", "grs", "p", "reverse"], reverse))