
from pyrogram import Client, filters
from pyrogram.types import(
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from RUKA.database import db, CACHE_USERS, CACHE_GROUPS


@Client.on_message(filters.group & filters.incoming, group=3)
async def watcher_cmd(client, message):
    try:
        user_id = message.from_user.id
        chat_id = message.chat.id
    except:
        return
        
    if user_id not in CACHE_USERS:
        name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
        user_name = message.from_user.username or "None"
        
        CACHE_USERS.append(user_id)
        await db.add_user(user_id, name, coins=0, is_scanned=False)

    if chat_id not in CACHE_GROUPS:
        name = message.chat.title
        user_name = message.chat.username or "None"
        member_count = await client.get_chat_members_count(chat_id)

        CACHE_GROUPS.append(chat_id)
        await db.add_group(chat_id, name, member_count, is_scanned=False)
