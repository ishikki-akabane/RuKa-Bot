"""
Made by Ishikki Akabane
Dont just kang or clone
Learn to value someone's hardwork, so please dont remove credits
Made with dedication and love
If you face any issues, feel free to visit @DevsLAB,
or into my DM to abuse me or for help or just to say thanks.
Thankyou if you read this notice fully :), have a wonderful cody day
"""


"""
This file imports all essential variables and functions, sets up logging, 
and initializes key components like the uptime tracker.
"""
import logging
import os
import sys
import time
import asyncio
import aiohttp
import json
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
SUDO_USERS = Config.SUDO_USERS
OWNER_ID = Config.OWNER_ID
SUPPORT_CHAT = Config.SUPPORT_CHAT
TOKEN_EXAMPLE = Config.TOKEN_EXAMPLE

LOGGER.info("[SERVER] - All variables successfully loaded")

"""
ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None) # Bot Token

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
        GUARDIAN_USERS = set(int(x) for x in os.environ.get("GUARDIAN_USERS", "").split())
        ENFORCER_USERS = set(int(x) for x in os.environ.get("ENFORCER_USERS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your super userlist does not contain valid integers")

    # Login to https://my.telegram.org and create a app
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)

    # IMPORTANT VARIABLES
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "DevsLab")      # Support group for users
    SUPPORT_ID = int(os.environ.get("SUPPORT_ID", "-100"))        # Support group id
    JOIN_LOGGER = int(os.environ.get("JOIN_LOGGER", "-100"))      # channel where the bot will send new chat joined messages
    EVENT_LOGS = int(os.environ.get("EVENT_LOGS", "-100"))        # channel where the bot will print stuffs like gban messages
    ERROR_LOGS = int(os.environ.get("ERROR_LOGS", "-100"))        # channel where the bot will print error when it encounters it
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "UpdatesXD")     # Channel where users can read about new updates about the bot
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Ishikki_AKabane") # Owner UserName without @

    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")

    # Database | Ignore if you dont have and use public database of @ishikki_akabane
    DB_URI = os.environ.get("DATABASE_URL", "postgres://cugocwks:jgpqMTLw2rO6KMwnWDL6kAXwmaVMB1qW@john.db.elephantsql.com/cugocwks") #SQL DATABASE
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None) #MongoDB database
    REDIS_URL = os.environ.get("REDIS_URL", "redis://ishikki:Ishikki_143@redis-11102.c264.ap-south-1-1.ec2.cloud.redislabs.com:11102/") #Redis Database

    # Optional
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    BLUE_API = os.environ.get("BLUE_API", None)
    BLUE_URL = os.environ.get("BLUE_URL", "https://blue-api.vercel.app")
    
    # IF YOU WANT TO ALLOW GROUPS TO ADD BOT IN THE CHAT GROUPS,THEN SET IT TRUE
    ALLOW_CHATS = bool(os.environ.get("ALLOW_CHATS", True))
    INFOPIC = bool(os.environ.get("INFOPIC", True))

else:
    from RUKA.config import Development as Config

    TOKEN = Config.TOKEN #Bot Token

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer")
    
    try:
        WHITE_USERS = set(int(x) for x in Config.WHITE_USERS or [])
        SUPPORT_USERS = set(int(x) for x in Config.SUPPORT_USERS or [])
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your support or sudo or dev users list does not contain valid integers.")

    # FOR TELETHON AND PYROGRAM BASED BOTS, Login to https://my.telegram.org and fill it
    API_ID = int(Config.API_ID)
    API_HASH = Config.API_HASH

    # IMPORTANT VARIABLES
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SUPPORT_ID = Config.SUPPORT_ID
    JOIN_LOGGER = Config.JOIN_LOGGER #channel where the bot will send new chat joined messages
    EVENT_LOGS = Config.EVENT_LOGS #channel where the bot will print stuffs like gban messages
    ERROR_LOGS = Config.ERROR_LOGS #channel where the bot will print error when it encounters it
    UPDATES_CHANNEL = Config.UPDATES_CHANNEL #Channel where they can read about new updates about the bot
    OWNER_USERNAME = Config.OWNER_USERNAME

    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
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
    DB_URI = Config.DATABASE_URI #SQL DATABASE
    MONGO_DB_URI = Config.MONGO_DB_URI #MongoDB database
    REDIS_URL = Config.REDIS_URL #Redis Database

    # Optional
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALLPAPERS_API
    BLUE_API = Config.BLUE_API
    BLUE_URL = Config.BLUE_URL
    
    # IF YOU WANT TO ALLOW GROUPS TO ADD BOT IN THE CHAT GROUPS,THEN SET IT TRUE
    ALLOW_CHATS = Config.ALLOW_CHATS
    INFOPIC = Config.INFOPIC

LOGGER.info("[VARIABLES LOADED] - All variables successfully loaded")
#=======================================================================================================X
DEV_USERS = list(DEV_USERS)
SUDO_USERS = list(SUDO_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)
WHITE_USERS = list(WHITE_USERS)

DEV_USERS.append(OWNER_ID)
#=======================================================================================================X
class ISHIKKI_IMAGE():
    RUKA_IMG_START = "https://graph.org/file/653341f199df582194481.mp4"
    RUKA_STARTUP_PIC = "https://graph.org/file/644b74fb6d35e863f1590.jpg"
#=======================================================================================================X
bot_alive_msg = "Ruka is now Alive"

aiosession = aiohttp.ClientSession()


async def booting_msg(application: Application):
    bot = Bot(token=TOKEN)
    await bot.initialize()
    url = BLUE_URL + "/connect"
    headers = {"API-KEY": BLUE_API}
    data = {"bot": {"id": bot.id, "username": bot.username}, "owner": {"owner_id": OWNER_ID, "owner_username": OWNER_USERNAME}}
    try:
        async with aiosession.post(url, headers=headers, json=data) as resp:
            response = await resp.json()
        LOGGER.info(response["msg"])
    except:
        LOGGER.info("[BLUE-API] - Blue-API FAiled To STARTUP!! REPORT TO @DEVSLAB")
    try:
        #await application.bot.sendPhoto(chat_id=SUPPORT_ID, photo=ISHIKKI_IMAGE.RUKA_STARTUP_PIC, caption=bot_alive_msg)
        n = 4
    except Exception as e:
        LOGGER.warning(
            "[ERROR] - Bot isn't able to send message to support_chat!",
        )
        print(e)

#=======================================================================================================X

# Build dispatcher object for python-telegram-bot
dp = ApplicationBuilder().token(TOKEN).post_init(booting_msg).build()
"""
