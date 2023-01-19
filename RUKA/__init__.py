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


# Enable Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)


# Python version must be above or equal to 3.7
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.9! Multiple features depend on this. Bot quitting.",
    )
    quit(1)


# Starts the clock to note since how long the bot is running
StartTime = time.time()


TOKEN = "5312061963:AAEI3ug5nKWG_3t_ZZ1SWwH2T8ab8D1Azfg"


application = ApplicationBuilder().token(TOKEN).build()
asyncio.get_event_loop().run_until_complete(application.bot.initialize())