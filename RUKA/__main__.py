"""
Main entry point for the Advanced Telegram Group Management Bot

This script initializes and starts the bot, handles errors gracefully, and ensures
efficient execution using uvloop for better performance.
"""

import asyncio
import uvloop
from pyrogram import Client
import traceback
import requests

from . import LOGGER, TOKEN, API_HASH, API_ID, SUPPORT_CHAT

class Bot(Client):
    def __init__(self):
        super().__init__(
            "RUKAPROBOT",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins={"root": "RUKA.plugins"},
        )
    
    async def start(self):
        await super().start()
        me = await self.get_me()  # Fetch bot information to confirm successful start
        LOGGER.info(f"{me.first_name} (@{me.username}) started successfully.")

        # Notify the support chat that the bot has started
        try:
            await self.send_message(SUPPORT_CHAT, f"{me.first_name} has started successfully!")
        except Exception as e:
            LOGGER.error(f"Failed to send start message to support chat: {e}")
            LOGGER.debug(traceback.format_exc())

    async def stop(self):
        await super().stop()
    
    async def run_bot(self):
        try:
            await self.start()
            await idle()  # Keep the bot running until interrupted
        except (KeyboardInterrupt, SystemExit):
            LOGGER.warning("Bot stopped by user.")
        finally:
            await self.stop()

if __name__ == "__main__":
    uvloop.install()
    Bot().run()


"""
import time
import importlib
import os

from RUKA import dp, LOGGER, StartTime, OWNER_USERNAME, SUPPORT_CHAT, BLUE_API, aiosession, OWNER_ID, ISHIKKI_IMAGE
from RUKA.tools.time import get_readable_time
from RUKA.modules import ALL_MODULES
from RUKA.helpers.help_section import create_menu

from RUKA.database.sql.user_sql import sql_adduser

from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Chat, User
from telegram.constants import ParseMode
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Forbidden,
)


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("RUKA.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
"""
#====================================================
START_TXT = """
Im alive master, still in development.
It is gonna be an open source public group managment bot with all latest features and modules.

- My developer: @ishikki_akabane
- Alive since {}
"""

HELP_TXT = """
wait, bot is still in developement

visit @devslab
or contact @ishikki_akabane
"""

ABOUT_TXT = """
waitooooo broo
bot is still in development
:)
"""
#====================================================

"""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    uptime = get_readable_time((time.time() - StartTime))

    if update.effective_chat.type == "private":
        await message.reply_video(
            video=ISHIKKI_IMAGE.RUKA_IMG_START,
            caption=START_TXT.format(uptime),
            #parse_mode=ParseMode.MARKDOWN,
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
                        InlineKeyboardButton(text="ABOUT", callback_data="ishikki=about")
                    ],
                    [
                        InlineKeyboardButton(text="updates", url="t.me/updatesxd"),
                        InlineKeyboardButton(text="commands", callback_data="ishikki=help")
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
    keyboard = await create_menu()
    await message.reply_video(
        video=ISHIKKI_IMAGE.RUKA_IMG_START,
        caption=HELP_TXT,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard
    )


# Define the callback function for handling button presses
async def button_callback(update, context):
    query = update.callback_query
    data = query.data
    if data.split("=")[0] == "module":
        # Get the module name from the button data
        module_name = data.split('=')[1]
        # Load the module dynamically
        module = importlib.import_module(f'RUKA.modules.{module_name}')
        # Get the value of the __help__ variable from the module
        help_text = getattr(module, '__help__', 'No help available.')
        # Edit the message with the help text
        await query.edit_message_caption(
            caption=help_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Back", callback_data="ishikki=help")]
                ]
            )
        )
    elif data.split("=")[0] == "ishikki":
        if data.split("=")[1] == "help":
            keyboard = await create_menu()
            await query.edit_message_caption(
                caption=HELP_TXT,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=keyboard
            )
        elif data.split("=")[1] == "about":
            await query.edit_message_caption(
                caption=ABOUT_TXT,
                parse_mode=ParseMode.MARKDOWN
            )
        elif data.split("=")[1] == "back_btn":
            uptime = get_readable_time((time.time() - StartTime))
            await query.edit_message_caption(
                caption=START_TXT.format(uptime),
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
                            InlineKeyboardButton(text="ABOUT", callback_data="ishikki=about")
                        ],
                        [
                            InlineKeyboardButton(text="updates", url="t.me/updatesxd"),
                            InlineKeyboardButton(text="commands", callback_data="ishikki=help")
                        ]
                    ]
                )
            )
        else:
            await query.edit_message_caption(
                caption=ABOUT_TXT,
                parse_mode=ParseMode.MARKDOWN
            )
    else:
        return


# ERROR HANDLER
async def error_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    error = context.error
    try:
        raise error
    except Forbidden:
        LOGGER.error("\nForbidden Error\n")
        LOGGER.error(error)
        raise error
        # remove update.message.chat_id from conversation list
    except BadRequest:
        LOGGER.error("\nBadRequest Error\n")
        LOGGER.error("BadRequest caught")
        LOGGER.error(error)
        raise error

        # handle malformed requests - read more below!
    except TimedOut:
        LOGGER.error("\nTimedOut Error\n")
        raise error
        # handle slow connection problems
    except NetworkError:
        LOGGER.error("\n NetWork Error\n")
        raise error
        # handle other connection problems
    except ChatMigrated as err:
        LOGGER.error("\n ChatMigrated error\n")
        raise error
        LOGGER.error(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        LOGGER.error(error)
        raise # then only it sends the message to the owner
        # handle all other telegram related errors


def main():

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help_cmd)
    # Register the button callback handler
    dp.add_handler(CallbackQueryHandler(button_callback, block=False))
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    dp.add_error_handler(error_callback)

    LOGGER.info("Ruka is now deployed!!!\n->->->-Using long polling...")
    dp.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded all modules")
    main()
"""
