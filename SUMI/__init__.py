import logging
import os
import sys
import time
import spamwatch
import aiohttp
import telegram.ext as tg
from telethon.sessions import StringSession
from telethon import TelegramClient
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from redis import StrictRedis
from Python_ARQ import ARQ
from pyrogram import Client, errors
from SUMI.services.quoteapi import Quotly

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger("[SUMI]")

log = logging.getLogger('[Your Bot Is DEPLOYING]')

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.]"
    )
    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)

    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get('JOIN_LOGGER', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "5030730429").split())
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get('INFOPIC', True))
    EVENT_LOGS = os.environ.get('EVENT_LOGS', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://thearq.tech")
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", None)
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get('API_ID', None)
    API_HASH = os.environ.get('API_HASH', None)
    DB_URI = os.environ.get('DATABASE_URL')
    DONATION_LINK = os.environ.get('DONATION_LINK', "https//t.me/ishikki_akabane")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', True))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = os.environ.get('BAN_STICKER',
                                 'CAADAgADOwADPPEcAXkko5EB3YGYAg')
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    CASH_API_KEY = os.environ.get('CASH_API_KEY', None)
    TIME_API_KEY = os.environ.get('TIME_API_KEY', None)
    AI_API_KEY = os.environ.get('AI_API_KEY', None)
    WALL_API = os.environ.get('WALL_API', None)
    SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', "suppporttxd")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get('SPAMWATCH_SUPPORT_CHAT', "suppporttxd")
    SPAMWATCH_API = os.environ.get('SPAMWATCH_API', "dy9YPcbKyJ6IweLQhyllS6IdGfItDaAMh746uH7dDAXuTBdjyucnX2cGgFLUD~UD")
    BANCODES = os.environ.get("BANCODES", "You want me to ban the person who created my codes! ARE YOU CRAZY!!!!")
    REPOSITORY = os.environ.get("REPOSITORY", "https://github.com/Ishikki-Akabane/SUMI")
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "IshikkiAkabane")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    BOT_NAME = os.environ.get("BOT_NAME", None) # Name Of your Bot
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Bot Username
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
    LOG_GROUP_ID = os.environ.get('LOG_GROUP_ID', None)
    ERROR_LOGS = os.environ.get("ERROR_LOGS", None) # Error Logs (Channel Ya Group Choice Is Yours) (-100)
    STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', True))
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://ishikki:rohanj143@cluster0.aygtdie.mongodb.net/?retryWrites=true&w=majority") #Use IT Wisely 
    DEBUG = bool(os.environ.get('IS_DEBUG', False))
    REDIS_URL = os.environ.get("REDIS_URL", "redis://kazumaclan:Ishikki@143@redis-17153.c264.ap-south-1-1.ec2.cloud.redislabs.com:17153") # REDIS URL (From:- Heroku & Redis)
    OWNER_NAME = os.environ.get("OWNER_NAME", None)
    COTB = os.environ.get("COTB", "Ishikki_Akabane")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "updatesxd")
    NETWORK_USERNAME = os.environ.get("NETWORK_USERNAME", "KazumaClanXD")
    NETWORK_NAME = os.environ.get("NETWORK_NAME", "KAZUMA CLAN")
    AFKVID = os.environ.get("SUMI_AFKVID", "")
    GROUP_ALIVE_PIC = os.environ.get("SUMI_GROUP_ALIVE_PIC", "")
    SUMI_DISPACHER_PIC = os.environ.get("SUMI_DISPACHER_PIC", "")
    SUMI_HELP_PIC = os.environ.get("SUMI_HELP_PIC", "")
    PM_IMAGE = os.environ.get("SUMI_PM_IMAGE", "")
    GROUPSTART_VID = os.environ.get("SUMI_GROUPSTART_VID", "")
    SUMI_OWNER_WEL_IMG = os.environ.get("SUMI_OWNER_WEL_IMG", "")
    SUMI_DIS_WEL = os.environ.get("SUMI_DIS_WEL", "")
    SUMI_WELCOME = os.environ.get("SUMI_WELCOME", "")
    SUMI_STATS_PIC = os.environ.get("SUMI_STATS_PIC", "")


    try:
        BL_CHATS = set(int(x) for x in os.environ.get('BL_CHATS', "").split())
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")
    
else:
    from SUMI.config import Development as Config
    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [5030730429])
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    INFOPIC = Config.INFOPIC
    ARQ_API_URL = Config.ARQ_API_URL
    ARQ_API_KEY = Config.ARQ_API_KEY
    BOT_NAME = Config.BOT_NAME
    BOT_USERNAME = Config.BOT_USERNAME
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    LOG_GROUP_ID = Config.LOG_GROUP_ID
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    ERROR_LOGS = Config.ERROR_LOGS
    STRICT_GMUTE = Config.STRICT_GMUTE
    UPDATE_CHANNEL = Config.UPDATE_CHANNEL
    REDIS_URL = Config.REDIS_URL
    NETWORK_USERNAME = Config.NETWORK_USERNAME
    NETWORK_NAME = Config.NETWORK_NAME
    AFKVID = Config.AFKVID
    GROUP_ALIVE_PIC = Config.GROUP_ALIVE_PIC
    SUMI_STATS_PIC = Config.SUMI_STATS_PIC
    SUMI_WELCOME = Config.SUMI_WELCOME
    SUMI_DIS_WEL = Config.SUMI_DIS_WEL
    SUMI_OWNER_WEL_IMG = Config.SUMI_OWNER_WEL_IMG
    SUMI_DISPACHER_PIC = Config.SUMI_DISPACHER_PIC
    SUMI_HELP_PIC = Config.SUMI_HELP_PIC
    PM_IMAGE = Config.PM_IMAGE
    GROUPSTART_VID = Config.GROUPSTART_VID

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key Expired Or Losted!")
    
else:
    sw = spamwatch.Client(SPAMWATCH_API)

session_name = TOKEN.split(":")[0]
pgram = Client(session_name, api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

#install aiohttp session
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession() 

#install arq
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("SUMI", API_ID, API_HASH)
pbot = Client("SumiXDbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
mongo_client = MongoClient(MONGO_DB_URI)
dispatcher = updater.dispatcher

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

#-------Quote-------
quotly = Quotly()
#-------------------

# Load at end to ensure all prev variables have been set
from SUMI.modules.helper_funcs.handlers import (CustomCommandHandler,
                                                        CustomMessageHandler,
                                                        CustomRegexHandler)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

print("Connecting Pyrogram Client")
pgram.start()

print("Checking Errors")

bottie = pgram.get_me()

BOT_ID = bottie.id
BOT_USERNAME = bottie.username
BOT_NAME = bottie.first_name
BOT_MENTION = bottie.mention



REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)

try:

    REDIS.ping()

    LOGGER.info("[SUMI]:Connecting To Redis Database")

except BaseException:

    raise Exception("[ERROR]: Your Redis Database Is Not Alive, Please Check Again.")

finally:

   REDIS.ping()
