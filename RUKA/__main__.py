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
import os

from RUKA import dp, LOGGER, StartTime, OWNER_USERNAME, SUPPORT_CHAT, BLUE_API, aiosession, OWNER_ID
from RUKA.tools.time import get_readable_time
from RUKA.modules import ALL_MODULES
from RUKA.helpers.help_section import create_menu

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
                        InlineKeyboardButton(text="OWNER", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="ABOUT", url="t.me/")
                    ],
                    [
                        InlineKeyboardButton(text="updates", url="t.me/updatesxd"),
                        InlineKeyboardButton(text="commands", url="t.me/")
                    ]
                ]
            )
        )
    else:
        await message.reply_text(
            f"I'm Alive, working since {uptime}"
        )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    keyboard = create_menu()
    await message.reply_text(
        "help section",
        reply_markup=keyboard
    )


# Define the callback function for handling button presses
async def button_callback(update, context):
    query = update.callback_query
    data = query.data

    # Get the module name from the button data
    module_name = data.split(':')[1]

    # Load the module dynamically
    module = importlib.import_module(f'RUKA.modules.{module_name}')

    # Get the value of the __help__ variable from the module
    help_text = getattr(module, '__help__', 'No help available.')

    # Edit the message with the help text
    await context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=help_text)


def main():

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help_cmd)
    # Register the button callback handler
    dp.add_handler(CallbackQueryHandler(button_callback))
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)

    LOGGER.info("Ruka is now deployed!!!\n----Using long polling...")
    dp.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded all modules")
    main()