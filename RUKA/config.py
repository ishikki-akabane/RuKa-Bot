import json
import os


class Config(object):
    LOGGER = True
    # REQUIRED

    # Login to https://my.telegram.org and fill in these slots with the details given by it
    API_ID = 123456
    API_HASH = "d3a6dbd3e466159f7170f6af7fb3fgfgf"

    TOKEN = "BOT_TOKEN"  # BOT TOKEN, get it from @botfather
    OWNER_ID = "5030730429"  # If you dont know, run @KAZUMABOT and send /id
    OWNER_USERNAME = "Ishikki_AKABANE" #OWNER Username without @

    SUPPORT_CHAT = "DevsLAB"  # Your own group for support, do not add the @
    JOIN_LOGGER = (-1001253661229)  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (-1001190806654)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging
    ERROR_LOGS = (-1001212354666)  # Prints error info
    UPDATES_CHANNEL = "UpdatesXD" #Channel where they can read about new updates about the bot
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8 # Number of subthreads to use. Set as number of threads your processor uses
    ALLOW_EXCL = True
    # For ARQ based Modules, use public ARQ KEY if you dont have @ISHIKKI_AKABANE
    ARQ_API_KEY = "ZWXCEZ-RTVXHT-NOVURC-FHCFZD-ARQ"
    # For SPAMWATCH ANTISPAM SYSTEM, USE PUBLIC ONE IF YOU DONT HAVE
    SPAMWATCH_SUPPORT_CHAT = "@DEVSLAB"
    SPAMWATCH_API = "XChWQMRDLpKVqoirR_cMDqlrGwiTn1bY1pYhTyGeVv7~T2gVG1JRyZFvlZGq4gtG"

    # Important for webhooks
    WEBHOOK = False
    URL = None
    PORT = 5000
    CERT_PATH = None
    
    #DATABASE | Ignore if you dont have and use public database of @ishikki_akabane
    DATABASE_URI = ""  # needed for any database modules, recommended to use PostgreSQL or ElephantSQL
    MONGO_DB_URI = "" #MongoDB
    REDIS_URL = "" #Redis

    # OPTIONAL | Ignore if you dont have and use public API KEY's of @ishikki_akabane
    # For WEATHER, Get Your API key from https://openweathermap.org/api
    OPENWEATHERMAP_ID = ""
    # For CASH, Get your API key from https://www.alphavantage.co/support/#api-key
    CASH_API_KEY = "V7NS1NBFEL4X24L6"
    # For TIME, Get your API key from https://timezonedb.com/api
    TIME_API_KEY = "2AS711XS1O9B"
    AI_API_KEY = "lol"
    # For wallpapers, get one from https://wall.alphacoders.com/api.php
    WALLPAPERS_API = "lol"

    # IF YOU WANT TO ALLOW GROUPS TO ADD BOT IN THE CHAT GROUPS,THEN SET IT TRUE
    ALLOW_CHATS = True


    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SUPPORT_USERS = [] #give comma after each ID
    #List of id's (not usernames) for users which are allowed to gban and also have many rights
    SUDO_USERS = [] #give comma after each ID
    #List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [] #give comma after each ID


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True