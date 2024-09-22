

import logging
import os
import sys
import time
from .config import Config
from MeowCore import MeowCore


# Enable Logging ========================================================================================X
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)


# Python version must be above or equal to 3.7 ==========================================================X
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.7! Multiple features depend on this. Bot quitting.",
    )
    quit(1)


# Starts the clock to note since how long the bot is running ============================================X
StartTime = time.time()


# ENVIRONMENT VARIABLE ==================================================================================X
TOKEN = Config.TOKEN
API_ID = Config.API_ID
API_HASH = Config.API_HASH
DATABASE_URL = Config.DATABASE_URL
LOG_CHANNEL = Config.LOG_CHANNEL
ERROR_LOG_CHANNEL = Config.ERROR_LOG_CHANNEL
DEV_USERS = Config.DEV_USERS
OWNER_ID = Config.OWNER_ID
SUPPORT_CHAT = Config.SUPPORT_CHAT
SUPPORT_CHAT_ID = Config.SUPPORT_CHAT_ID
MEOWCORE_TOKEN = Config.MEOWCORE_TOKEN

BOT_USERNAME = Config.BOT_USERNAME
BOT_ID = int(TOKEN.split(":")[0])

#TOKEN_EXAMPLE = Config.TOKEN_EXAMPLE

LOGGER.info("[SERVER] - All variables successfully loaded")


# INSTALLING OF MEOWCORE PLUGIN =========================================================================X

"""
MeowClient = MeowCore(
    MEOWCORE_TOKEN,
    category="telegram",
    bot_id=BOT_ID,
    bot_username=BOT_USERNAME
)
"""
