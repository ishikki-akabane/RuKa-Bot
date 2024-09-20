

from pyrogram import Client, filters

#@Client.on_message(filters.new_chat_members, group=3)
async def welcome_cmd(client, message):
    new_members = message.new_chat_members
    for member in new_members:
        bot_id = 123456789
        if bot_id == member.id:
            pass
