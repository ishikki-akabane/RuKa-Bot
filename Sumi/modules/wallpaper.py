from random import randint

import requests as r
from Sumi import SUPPORT_CHAT, WALL_API, dispatcher
from Sumi.modules.disable import DisableAbleCommandHandler
from Sumi.modules.sql.clear_cmd_sql import get_clearcmd
from Sumi.modules.helper_funcs.misc import delete
from telegram import Update
from telegram.ext import CallbackContext, run_async

# Wallpapers module by @TheRealPhoenix using wall.alphacoders.com


def wall(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    args = context.args
    msg_id = update.effective_message.message_id
    bot = context.bot
    query = " ".join(args)
    if not query:
        msg.reply_text("Please enter a query!")
        return
    else:
        caption = query
        term = query.replace(" ", "%20")
        json_rep = r.get(
            f"https://wall.alphacoders.com/api2.0/get.php?auth={WALL_API}&method=search&term={term}"
        ).json()
        if not json_rep.get("success"):
            msg.reply_text(f"An error occurred! Report this @{SUPPORT_CHAT}")
        else:
            wallpapers = json_rep.get("wallpapers")
            if not wallpapers:
                msg.reply_text("No results found! Refine your search.")
                return
            else:
                index = randint(0, len(wallpapers) - 1)  # Choose random index
                wallpaper = wallpapers[index]
                wallpaper = wallpaper.get("url_image")
                wallpaper = wallpaper.replace("\\", "")
                delmsg_preview = bot.send_photo(
                    chat_id,
                    photo=wallpaper,
                    caption="Preview",
                    reply_to_message_id=msg_id,
                    timeout=60,
                )
                delmsg = bot.send_document(
                    chat_id,
                    document=wallpaper,
                    filename="wallpaper",
                    caption=caption,
                    reply_to_message_id=msg_id,
                    timeout=60,
                )

    cleartime = get_clearcmd(chat_id, "wall")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg_preview, cleartime.time)
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


WALLPAPER_HANDLER = DisableAbleCommandHandler("wall", wall, run_async=True)
dispatcher.add_handler(WALLPAPER_HANDLER)
