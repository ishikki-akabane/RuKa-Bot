import wikipedia, os, glob
from Sumi import dispatcher
from Sumi.modules.disable import DisableAbleCommandHandler
from Sumi.modules.helper_funcs.misc import delete
from Sumi.modules.sql.clear_cmd_sql import get_clearcmd
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from wikipedia.exceptions import DisambiguationError, PageError


def wiki(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = (
        update.effective_message.reply_to_message
        if update.effective_message.reply_to_message
        else update.effective_message
    )
    res = ""
    if msg == update.effective_message:
        search = msg.text.split(" ", maxsplit=1)[1]
    else:
        search = msg.text
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        delmsg = update.message.reply_text(
            "Disambiguated pages found! Adjust your query accordingly.\n<i>{}</i>".format(
                e
            ),
            parse_mode=ParseMode.HTML,
        )
    except PageError as e:
        delmsg = update.message.reply_text(
            "<code>{}</code>".format(e), parse_mode=ParseMode.HTML
        )
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">Read more...</a>"""
        if len(result) > 4000:
            with open("result.txt", "w") as f:
                f.write(f"{result}\n\nUwU OwO OmO UmU")
            with open("result.txt", "rb") as f:
                delmsg = context.bot.send_document(
                    document=f,
                    filename=f.name,
                    reply_to_message_id=update.message.message_id,
                    chat_id=update.effective_chat.id,
                    parse_mode=ParseMode.HTML,
                )

                try:
                    for f in glob.glob("result.txt"):
                        os.remove(f)
                except Exception:
                    pass

        else:
            delmsg = update.message.reply_text(
                result, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            )

    cleartime = get_clearcmd(chat.id, "wiki")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, run_async=True)
dispatcher.add_handler(WIKI_HANDLER)


__mod_name__ = "WiKi"


