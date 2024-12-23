from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPrivileges


async def check_permissions(client, chat_id, user_id, mode):
    member = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    if mode == "admin":
        if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            if member.privileges.can_restrict_members:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

async def check_admin(client, chat_id, user_id):
    member = await client.get_chat_member(chat_id=chat_id,user_id=user_id)
    if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return True
    else:
        return False
