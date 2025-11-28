"""
Bot Admin rights checking decorator for handlers.

This decorator:
- Determines if the bot is an admin in the CURRENT CHAT.
- Reads their admin permissions from ChatMember.privileges
- Matches permissions with required decorator rights.
- Supports msg=True/False to send deny messages or silently ignore.

Usage:
------
@botAdmin()
@botAdmin(rights="all", msg=True)
@botAdmin(rights=["can_delete_messages"], msg=True)

Valid RIGHTS:
- can_manage_chat
- can_delete_messages
- can_manage_video_chats
- can_restrict_members
- can_promote_members
- can_change_info
- can_post_messages
- can_edit_messages
- can_invite_users
- can_pin_messages
- is_anonymous
"""


from functools import wraps
from pyrogram.enums import ChatMemberStatus


def botAdmin(rights=None, msg: bool = False):
    """
    Ensure the BOT is an admin in the chat and optionally has specific rights.

    Parameters:
    -----------
    required_rights : None | str | list
        - None → bot must be admin (no rights required)
        - "all" → bot must have ALL admin rights
        - list → bot must have all listed rights (e.g. ["can_delete_messages"])
    msg : bool
        If True → sends a failure message.
        If False → silent return.
    """

    if isinstance(rights, str) and rights.lower() == "all":
        req = "all"
    elif isinstance(rights, str):
        req = [rights]
    elif isinstance(rights, list):
        req = rights
    else:
        req = None

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            chat_id = message.chat.id
            bot_id = client.me.id
            try:
                bot_member = await client.get_chat_member(chat_id, bot_id)
            except:
                if msg:
                    await message.reply_text("❌ Unable to verify bot admin status.")
                return
            if bot_member.status not in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                if msg:
                    await message.reply_text("❌ I must be an admin to use this command.")
                return
            privileges = bot_member.privileges
            rights_dict = {
                attr: getattr(privileges, attr)
                for attr in dir(privileges)
                if attr.startswith("can_")
            }
            if req == "all":
                missing = [r for r, val in rights_dict.items() if not val]
                if missing == ['can_edit_messages', 'can_post_messages']:
                    pass
                elif missing:
                    if msg:
                        await message.reply_text(
                            "❌ I am missing required admin rights:\n" +
                            "\n".join(f"- {m}" for m in missing)
                        )
                    return
                else:
                    pass
            elif isinstance(req, list):
                missing = [r for r in req if not rights_dict.get(r)]
                if missing:
                    if msg:
                        await message.reply_text(
                            f"❌ I need the right:\n- {missing[0]}"
                        )
                    return
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator


