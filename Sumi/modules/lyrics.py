from tswift import Song

from Sumi.modules.sql.clear_cmd_sql import get_clearcmd
from telegram import Bot, Update, Message, Chat
from telegram.ext import Updater, CommandHandler, CallbackContext, run_async
from Sumi import dispatcher
from Sumi.modules.disable import DisableAbleCommandHandler
from Sumi.modules.helper_funcs.misc import delete


def lyrics(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    query = message.text[len("/lyrics ") :]
    song = ""

    if query:
        song = Song.find_song(query)
        if song:
            if song.lyrics:
                msg = song.format()
            else:
                msg = "Couldn't find any lyrics for that song!"
        else:
            msg = "Song not found!"
        if len(msg) > 4090:
            with open("lyrics.txt", "w") as f:
                msg = f.write(f"{reply}\n\n\nOwO UwU OmO")
            with open("lyrics.txt", "rb") as f:
                msg = "Message length exceeded max limit! Sending as a text file."
    else:
        msg = "You haven't specified which song to look for!"

    delmsg = message.reply_text(
        text = msg,
        disable_web_page_preview = True,
    )

    cleartime = get_clearcmd(chat.id, "lyrics")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


LYRICS_HANDLER = DisableAbleCommandHandler("lyrics", lyrics, run_async=True)

dispatcher.add_handler(LYRICS_HANDLER)
