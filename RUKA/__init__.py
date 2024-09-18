

import logging
import os
import sys
import time
from .config import Config


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
BOT_USERNAME = Config.BOT_USERNAME
DATABASE_URL = Config.DATABASE_URL
LOG_CHANNEL = Config.LOG_CHANNEL
ERROR_LOG_CHANNEL = Config.ERROR_LOG_CHANNEL
DEV_USERS = Config.DEV_USERS
OWNER_ID = Config.OWNER_ID
SUPPORT_CHAT = Config.SUPPORT_CHAT
SUPPORT_CHAT_ID = Config.SUPPORT_CHAT_ID
#TOKEN_EXAMPLE = Config.TOKEN_EXAMPLE

LOGGER.info("[SERVER] - All variables successfully loaded")
