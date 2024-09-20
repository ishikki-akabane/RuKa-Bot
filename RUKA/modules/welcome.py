

from pyrogram import Client, filters

from RUKA import BOT_ID
from RUKA.database import db, CACHE_GROUPS


@Client.on_message(filters.new_chat_members, group=3)
async def welcome_cmd(client, message):
    new_members = message.new_chat_members
    for member in new_members:
        if BOT_ID == member.id:
            return
        
