"""
User-level access control decorator for Pyrogram command handlers.

Hierarchy (highest → lowest):
OWNER > DEV > SUDO > SUPPORT > WHITE

Usage:
------
@userLevel("OWNER", msg=True)
"""

from functools import wraps
from .. import CONFIG


LEVELS = {
    "OWNER": 5,
    "DEV": 4,
    "SUDO": 3,
    "SUPPORT": 2,
    "WHITE": 1,
}

LEVEL_MAP = {
    "OWNER": lambda: CONFIG.OWNER_LIST,
    "DEV": lambda: CONFIG.DEV_LIST,
    "SUDO": lambda: CONFIG.SUDO_LIST,
    "SUPPORT": lambda: CONFIG.SUPPORT_LIST,
    "WHITE": lambda: CONFIG.WHITE_LIST,
}


def get_user_level(user_id: int) -> int:
    """
    Returns numeric hierarchy level for user_id.
    Highest = 5 (OWNER), Lowest = 1 (WHITE), 0 = No level.
    """
    for level_name, getter in LEVEL_MAP.items():
        if user_id in getter():
            return LEVELS[level_name]
    return 0  # User not found in any list


def userLevel(required_level: str, msg: bool = False):
    """
    Decorator to restrict access to a handler based on user level.

    Parameters:
    -----------
    required_level : str
        One of: "OWNER", "DEV", "SUDO", "SUPPORT", "WHITE"
    msg : bool
        If True, sends a denial message to the user.
        If False, silently blocks without responding.
    """
    required_level = required_level.upper()
    if required_level not in LEVELS:
        raise ValueError(
            f"Invalid user level '{required_level}'. "
            f"Valid levels: {', '.join(LEVELS.keys())}"
        )
    required_rank = LEVELS[required_level]

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            user_id = message.from_user.id
            user_rank = get_user_level(user_id)
            if user_rank < required_rank:
                if msg:
                    allowed_label = required_level.capitalize()
                    await message.reply_text(
                        f"❌ You do not have access to this command.\n"
                        f"Required level: **{allowed_label}**."
                    )
                return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator

