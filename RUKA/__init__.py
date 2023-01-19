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
        raise Exception("Your OWNER_ID env variable is not a valid integer")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your support or sudo or dev users list does not contain valid integers")

    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)

    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "DevsLab")
    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None) #channel where the bot will send new chat joined messages
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None) #channel where the bot will print stuffs like gban messages
    ERROR_LOGS = os.environ.get("ERROR_LOGS", None) #channel where the bot will print error when it encounters it
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Ishikki AKabane")
    INFOPIC = bool(os.environ.get("INFOPIC", True))
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    # For ARQ based Modules, use public ARQ KEY if you dont have @ISHIKKI_AKABANE
    ARQ_API_KEY = "ZWXCEZ-RTVXHT-NOVURC-FHCFZD-ARQ"
    ARQ_API_URL = "https://thearq.tech"
    # For SPAMWATCH ANTISPAM SYSTEM, USE PUBLIC ONE IF YOU DONT HAVE
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", "XChWQMRDLpKVqoirR_cMDqlrGwiTn1bY1pYhTyGeVv7~T2gVG1JRyZFvlZGq4gtG")

    # Important for webhooks
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token, contains your app url
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")

    # Database | Ignore if you dont have and use public database of @ishikki_akabane
    DB_URI = os.environ.get("DATABASE_URL", "") #SQL DATABASE
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None) #MongoDB database
    REDIS_URL = os.environ.get("REDIS_URL", "redis://ishikki:Ishikki_143@redis-11102.c264.ap-south-1-1.ec2.cloud.redislabs.com:11102/") #Redis Database

    # If using Heroku
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)

    # Optional
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    
    # IF YOU WANT TO ALLOW GROUPS TO ADD BOT IN THE CHAT GROUPS,THEN SET IT TRUE
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)

else:
    from RUKA.config import Development as Config

    TOKEN = Config.TOKEN #Bot Token

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer")
    
    try:
        SUPPORT_USERS = set(int(x) for x in Config.SUPPORT_USERS or [])
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your support or sudo or dev users list does not contain valid integers.")

    API_ID = Config.API_ID
    API_HASH = API_HASH

    SUPPORT_CHAT = Config.SUPPORT_CHAT
    JOIN_LOGGER = Config.JOIN_LOGGER #channel where the bot will send new chat joined messages
    EVENT_LOGS = Config.EVENT_LOGS #channel where the bot will print stuffs like gban messages
    ERROR_LOGS = Config.ERROR_LOGS #channel where the bot will print error when it encounters it
    OWNER_USERNAME = Config.OWNER_USERNAME
    INFOPIC = Config.INFOPIC
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL
    # For ARQ based Modules, use public ARQ KEY if you dont have @ISHIKKI_AKABANE
    ARQ_API_KEY = Config.ARQ_API_KEY
    ARQ_API_URL = "https://thearq.tech"
    # For SPAMWATCH ANTISPAM SYSTEM, USE PUBLIC ONE IF YOU DONT HAVE
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API

    # Important for webhooks
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL  # Does not contain token, contains your app url
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    # Database | Ignore if you dont have and use public database of @ishikki_akabane
    DB_URI = Config.DATABASE_URL #SQL DATABASE
    MONGO_DB_URI = Config.MONGO_DB_URI #MongoDB database
    REDIS_URL = Config.REDIS_URL #Redis Database

    # If using Heroku
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME

    # Optional
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    VIRUS_API_KEY = Config.VIRUS_API_KEY
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALL_API
    
    # IF YOU WANT TO ALLOW GROUPS TO ADD BOT IN THE CHAT GROUPS,THEN SET IT TRUE
    ALLOW_CHATS = Config.ALLOW_CHATS



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
