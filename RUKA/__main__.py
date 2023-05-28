"""
Made by Ishikki Akabane
Dont just kang or clone
Learn to value someone's hardwork, so please dont remove credits
Made with dedication and love
If you face any issues, feel free to visit @DevsLAB,
or into my DM to abuse me or for help or just to say thanks.
Thankyou if read this notice fully :), have a wonderful cody day
"""
import time
import importlib

from RUKA import dp, LOGGER, StartTime, OWNER_USERNAME, SUPPORT_CHAT, BLUE_API, aiosession
from RUKA.tools.time import get_readable_time
from RUKA.modules import ALL_MODULES

from RUKA.database.sql.user_sql import sql_adduser

from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Chat, User
from telegram.constants import ParseMode



for module_name in ALL_MODULES:
    imported_module = importlib.import_module("RUKA.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    uptime = get_readable_time((time.time() - StartTime))

    if update.effective_chat.type == "private":
        await message.reply_text(
            "Im alive master, still in development.\nAlive since {}".format(uptime),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="☑ ᴀᴅᴅ RᴜKᴀ ☑",
                            url="t.me/RukaProbot?startgroup=true"
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

    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)

    LOGGER.info("Ruka is now deployed!!!\n----Using long polling...")
    dp.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded all modules")
    main()