from RUKA import application, LOGGER, StartTime, OWNER_USERNAME, SUPPORT_CHAT
from RUKA.strings.main import PM_START_MSG
from RUKA.tools.time import get_readable_time

from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Chat, User
from telegram.constants import ParseMode


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    uptime = get_readable_time((time.time() - StartTime))

    if update.effective_chat.type == "private":
        await message.reply_text(
            PM_START_MSG.format(uptime),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="☑ ᴀᴅᴅ RᴜKᴀ ☑",
                            url="t.me/Rukaaxdbot?startgroup=true"
                        )
                    ],
                    [
                        InlineKeyboardButton(text="OWNER", url=f"t.me/{OWNER_USERNAME}"),
                        InlineKeyboardButton(text="ABOUT", url="t.me/")
                    ],
                    [
                        InlineKeyboardButton(text="updates", url="t.me/updatesxd"),
                        InlineKeyboardButton(text="help", url="t.me/")
                    ]
                ]
            )
        )
    else:
        await message.reply_text(
            f"I'm Alive, working since {uptime}"
        )


def main():
    if SUPPORT_CHAT is not None:
        try:
            application.bot.send_message(SUPPORT_CHAT, "Bot Build completed!!")
        except Forbidden:
            LOGGER.warning(
                "Bot isn't able to send message to support_chat, go and check!",
            )
        except BadRequest as e:
            LOGGER.warning(e.message)

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    LOGGER.info("Using long polling.")
    application.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: ")
    main()