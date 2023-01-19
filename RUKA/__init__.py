import logging
import os
import platform
import sys
import time
import telegram.ext as tg
import random
import asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.error import BadRequest, Forbidden

# Enable Logging========================================================X
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)

# Python version must be above or equal to 3.7==========================X
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.9! Multiple features depend on this. Bot quitting.",
    )
    quit(1)

# Starts the clock to note since how long the bot is running============X
StartTime = time.time()


# ENVIRONMENT VARIABLE==============================================X
ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None) #Bot Token

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None) #channel where the bot will send new chat joined messages
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None) #channel where the bot will print stuffs like gban messages
    ERROR_LOGS = os.environ.get("ERROR_LOGS", None) #channel where the bot will print error when it encounters it
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Ishikki AKabane")




else:
    try:
        from zerotwobot.config import Development as Config
    except:
        print("Can't import config!")


TOKEN = "5312061963:AAEI3ug5nKWG_3t_ZZ1SWwH2T8ab8D1Azfg"
SUPPORT_CHAT = -1001856564943


async def start_init(application: Application):
    try:
        await application.bot.send_message(SUPPORT_CHAT, "Bot Build Start....!!")
    except Forbidden:
        LOGGER.warning(
            "Bot isn't able to send message to support_chat, go and check!",
        )
    except BadRequest as e:
        LOGGER.warning(e.message)


# Build application for python-telegram-bot, similar to old version dispatcher and updater
application = ApplicationBuilder().token(TOKEN).post_init(start_init).build()
asyncio.get_event_loop().run_until_complete(application.bot.initialize())
