import os
from dotenv import load_dotenv



load_dotenv()



def _to_int(val: str | None) -> int | None:
    try:
        return int(val) if val is not None else None
    except Exception:
        return None



def _to_list(val: str | None, cast_int: bool = False) -> list:
    if not val:
        return []
    items = [x.strip() for x in val.split(",") if x.strip()]
    if cast_int:
        out = []
        for x in items:
            try:
                out.append(int(x))
            except Exception:
                continue
        return out
    return items



class CONFIG_CLASS:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = _to_int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")

    OWNER_LIST = _to_list(os.environ.get("OWNER_LIST"), cast_int=True)
    DEV_LIST = _to_list(os.environ.get("DEVLIST"), cast_int=True)
    SUDO_LIST = _to_list(os.environ.get("SUDOLIST"), cast_int=True)
    SUPPORT_LIST = _to_list(os.environ.get("SUPPORTLIST"), cast_int=True)
    WHITE_LIST = _to_list(os.environ.get("WHITELIST"), cast_int=True)

    SUPPORT_CHAT_ID = _to_int(os.environ.get("SUPPORT_CHAT_ID"))
    LOGS_CHANNEL = _to_int(os.environ.get("LOGS_CHANNEL"))
    GBAN_LOGS = _to_int(os.environ.get("GBAN_LOGS"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")

    DB_URL = os.environ.get("DB_URL") or os.environ.get("DB_URl")

    SERVER_LOG_BOT_TOKEN = os.environ.get("SERVER_LOG_BOT_TOKEN")

    MEOW_API_TOKEN = os.environ.get("MEOW_API_TOKEN")

    def __init__(self):
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required in environment variables!")
        if not self.API_ID:
            raise ValueError("API_ID is required and must be an integer!")
        if not self.API_HASH:
            raise ValueError("API_HASH is required!")
        if not self.DB_URL:
            raise ValueError("DB_URL is required!")


