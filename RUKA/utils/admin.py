"""
Admin rights checking decorator for Pyrogram handlers.

This decorator:
- Determines if the user is an admin in the CURRENT CHAT.
- Reads their admin permissions from ChatMember.privileges
- Matches permissions with required decorator rights.
- Supports msg=True/False to send deny messages or silently ignore.

Usage:
------
@admin()
@admin(rights="all", msg=True)
@admin(rights=["can_delete_messages"], msg=True)

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


def admin(rights=None, msg: bool = False):
    """
    Parameters:
    -----------
    rights : None | str | list
        - None → must be admin, no specific permissions required.
        - "all" → must have ALL admin rights.
        - list of strings → must have ALL listed Pyrogram admin privileges.
    msg : bool
        If True → reply with missing-right message
        If False → silently block.
    """

    # Normalize rights
    if isinstance(rights, str) and rights.lower() == "all":
        required_rights = "all"
    elif isinstance(rights, str):
        required_rights = [rights]
    elif isinstance(rights, list):
        required_rights = rights
    else:
        required_rights = None  # Means admin only

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            chat_id = message.chat.id
            user_id = message.from_user.id
            try:
                member = await client.get_chat_member(chat_id, user_id)
            except Exception:
                if msg:
                    await message.reply_text("❌ Could not determine your admin status.")
                return
            if member.status not in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                if msg:
                    await message.reply_text("❌ You must be an admin to use this command.")
                return
            if member.status == ChatMemberStatus.OWNER:
                user_priv = member.privileges
            else:
                user_priv = member.privileges
            user_priv_dict = {
                key: getattr(user_priv, key)
                for key in dir(user_priv)
                if key.startswith("can_")
            }
            if required_rights == "all":
                missing = [r for r, val in user_priv_dict.items() if not val]
                if missing:
                    if msg:
                        await message.reply_text(
                            "❌ You are missing required admin rights:\n"
                            + "\n".join(f"- {r}" for r in missing)
                        )
                    return
            elif isinstance(required_rights, list):
                missing = [
                    r for r in required_rights
                    if r not in user_priv_dict or not user_priv_dict[r]
                ]
                if missing:
                    if msg:
                        await message.reply_text(
                            "❌ Missing required admin permission:\n"
                            f"- {missing[0]}"
                        )
                    return
            # If rights=None → only admin status was needed
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
