

from pyrogram import Client, filters

from RUKA import BOT_ID
from RUKA.database import db, CACHE_GROUPS


db_structure = {
    "_id": -1002839304040,   # chat id
    "mode": "",              # template / text / image / video / audio / document
    "media_link": "",        # if media else None
    "text": "",              # text message else empty string
}

# Deprecated
# @Client.on_message(filters.new_chat_members, group=3)
@Client.on_chat_member_updated(filters.group, group=3)
async def welcome_cmd(client, member):
    chat_id = member.chat.id
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    if BOT_ID == user.id:
        await client.send_message(chat_id, "ruka hop in")
        return
    else:
        await client.send_message(chat_id, f"{user.first_name} hopped in")
        
