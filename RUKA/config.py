


import os
import json


def get_user_list(key):
    with open("users.json", "r") as json_file:
        return json.load(json_file)[key]


class Config:
    # Basic Bot Configuration
    TOKEN = os.getenv("TOKEN", "6208314828:AAFbTH1SjzlVrnNA6XlAeH9ehqTewiH_nNM")
    API_ID = int(os.getenv("API_ID", 18579066))
    API_HASH = os.getenv("API_HASH", "b6922d525d9c218cc237aa8f6e31e9a6")
    BOT_USERNAME = os.getenv("BOT_USERNAME", "RukaProBot")

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgres://user:password@host:port/database")

    # Logging and Monitoring
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001234567890"))  # Example: -1001234567890 (Private Channel ID)
    ERROR_LOG_CHANNEL = int(os.getenv("ERROR_LOG_CHANNEL", -1001552477173))
   
    # Access Control
    DEV_USERS = list(map(int, os.getenv("DEV_USERS", "").split(',')))
    OWNER_ID = int(os.getenv("OWNER_ID", 5030730429))

    # Optional Extras
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "BotsLabXd")  # Without '@'
    SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID", -1001703076744))
    
    # Additional API integrations
    BLUE_API = os.getenv("BLUE_API", "blue-ishikki-personal")
