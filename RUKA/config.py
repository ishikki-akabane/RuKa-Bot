


import os
import json


def get_user_list(key):
    with open("users.json", "r") as json_file:
        return json.load(json_file)[key]


class Config:
    # Basic Bot Configuration
    TOKEN = os.getenv("TOKEN", "your-bot-token-here")
    API_ID = int(os.getenv("API_ID", "your-api-id-here"))
    API_HASH = os.getenv("API_HASH", "your-api-hash-here")
    BOT_USERNAME = os.getenv("BOT_USERNAME", "your-bot-username-here")

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgres://user:password@host:port/database")

    # Logging and Monitoring
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001234567890"))  # Example: -1001234567890 (Private Channel ID)
    
    # Access Control
    DEV_USERS = list(map(int, os.getenv("DEV_USERS", "").split(',')))
    OWNER_ID = int(os.getenv("OWNER_ID", "your-owner-id-here"))

    # Optional Extras
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "your-support-chat-username")  # Without '@'
    
    # Additional API integrations
    BLUE_API = os.getenv("BLUE_API", "blue-ishikki-personal")
