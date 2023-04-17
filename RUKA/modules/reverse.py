import os

import requests
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from RUKA import dp

api_key = "ffd3c65c70cb445485db4b237cb8a471"

async def reverse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    chat_id = update.effective_chat.id
    rtmid = msg.message_id

    reply = msg.reply_to_message

    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
            new_id = reply.sticker.file_unique_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
            new_id = reply.photo[-1].file_unique_id
        else:
            await msg.reply_text("Reply To An Image Or Sticker To Lookup!")
            return
        
        print(file_id)
        print(new_id)

        file_path = os.path.join("temp", f"{new_id}.jpg")
        file_url = await context.bot.get_file(file_id).file_path

    else:
        await msg.reply_text(
            "Please Reply To A Sticker, Or An Image To Search It!",
            parse_mode=ParseMode.MARKDOWN,
        )
        return
        
    try:
        endpoint_url = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
        headers = {
            "Ocp-Apim-Subscription-Key": api_key,
            "Content-Type": "multipart/form-data",
        }
        params = {"knowledgeRequest": {"filters": {"site": "all"}}}
        files = {"image": ("image.png", requests.get(file_url).content, "image/png")}

        response = requests.post(
            endpoint_url, headers=headers, params=params, files=files
        )

        response_json = json.loads(response.content)
        captionslist = response_json["tags"][0]["actions"][4]["data"]["value"]
        text = ""
        for caption in captionslist[:2]:
            text += caption["displayText"]
            text += " "
        await msg.reply_text(text)
    except Exception as e:
        await msg.reply_text("Cant find anything!!")


dp.add_handler(CommandHandler("pp", reverse))