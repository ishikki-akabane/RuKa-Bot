

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus, ChatType

from RUKA import BOT_ID, LOG_CHANNEL, MeowClient
from RUKA.database import db, CACHE_GROUPS, WELCOME_IDS
from RUKA.helpers.error_logger import ErrorLogger


MeowClient.load_welcome(WELCOME_IDS)

db_structure = {
    "_id": -1002839304040,   # chat id
    "mode": "",              # template / text / image / video / audio / document
    "media_link": "",        # if media else None
    "text": "",              # text message else empty string
    "keyboard": ""           # reply_markup
}

# Deprecated
# @Client.on_message(filters.new_chat_members, group=3)


@Client.on_chat_member_updated(filters.group, group=3)
async def welcome_cmd(client, member):
    if (
        not member.new_chat_member 
        or member.new_chat_member.status in {ChatMemberStatus.BANNED, ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED} 
        or member.old_chat_member
    ):
        return

    chat_id = member.chat.id
    user = member.new_chat_member.user if member.new_chat_member else member.from_user

    welcome_data = await db.check_chat_welcome(chat_id)
    if welcome_data == None:
        return # will come back later on

    if welcome_data["mode"] == "template":
        template_id = welcome_data["template_id"]
        template_data = await initialise_welcome(template_id, client, user, chat)
        await MeowClient.build_welcome(
            template_id,
            user,
            chat,
            template_data
        )
    
    if user.id == BOT_ID:
        await client.send_message(chat_id, "ruka hop in")
    else:
        await client.send_photo(chat_id, photo=f"resources/{chat.id}complete.png", caption=f"{user.first_name} hopped in")
        

@Client.on_chat_member_updated(filters.group, group=4)
async def goodbye_cmd(client, member):
    if (
        not member.new_chat_member 
        and member.old_chat_member 
        and member.old_chat_member.status not in {ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED}
    ):
        pass
    else:
        return
        
    chat_id = member.chat.id
    user = member.old_chat_member.user if member.old_chat_member else member.from_user
    if user.id == BOT_ID:
        await client.send_message(
            LOG_CHANNEL,
            f"""
#CHATLEFT

**• ChatID:** __{chat_id}__
**• Name:** __{member.chat.title}__
"""
        )
    else:
        await client.send_message(chat_id, f"{user.first_name} byeee")


@Client.on_message(filters.group, filters.command("/welcome"))
@ErrorLogger
async def set_welcome(client, message):
    chat_id = message.chat.id
    await db.add_welcome(chat_id)
    await message.reply_text("successfully welcome set")


