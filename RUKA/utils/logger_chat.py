

from functools import wraps
from pyrogram.enums import ChatMemberStatus
from datetime import datetime
from RUKA import CONFIG


def loggerChat(mode: str):
    """
    Logs moderation events to LOGGER_CHAT_ID.

    Expected return from handler:
    {
        "target_id": int,
        "target_name": str,
        "reason": str | None
    }

    Modes:
    -------
    "ban", "mute", "kick", "warn", "promote",
    "demote", "welcome", "leave", "purge", "delete"
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):

            result = await func(client, message, *args, **kwargs)
            # Everything done → now log

            log_chat = CONFIG.LOGS_CHANNEL

            admin = message.from_user
            chat = message.chat

            # Default placeholders
            target_name = "-"
            target_id = "-"
            reason = "-"

            if isinstance(result, dict):
                target_name = result.get("target_name", target_name)
                target_id = result.get("target_id", target_id)
                reason = result.get("reason", reason)

            # Message link (works only in supergroups)
            link = None
            try:
                if chat.username:
                    link = f"https://t.me/{chat.username}/{message.id}"
                else:
                    # Private groups need their internal link format
                    link = f"https://t.me/c/{str(chat.id)[4:]}/{message.id}"
            except:
                link = "N/A"

            text = (
                f"📢 **Moderation Event: {mode.upper()}**\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"👮 **Admin:** {admin.mention} (`{admin.id}`)\n"
                f"👤 **Target:** {target_name} (`{target_id}`)\n"
                f"🛠 **Action:** `{mode}`\n"
                f"💬 **Chat:** {chat.title} (`{chat.id}`)\n"
                f"📝 **Reason:** {reason}\n"
                f"🔗 **Message:** [Jump to message]({link})\n"
                f"🕒 **Time:** `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`"
            )

            try:
                await client.send_message(
                    chat_id=log_chat,
                    text=text,
                    disable_web_page_preview=True
                )
            except:
                pass

            return result

        return wrapper
    return decorator
