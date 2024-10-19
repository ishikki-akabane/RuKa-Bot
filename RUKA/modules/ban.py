from pyrogram import Client, filters
from RUKA.helpers.error_logger import ErrorLogger
from RUKA.helpers.admin_func import check_permissions,check_admin


@Client.on_message(filters.command(["ban","unban"]))
@ErrorLogger
async def ban_cmd(client,message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot_id = (await client.get_me()).id
    check_bot = await check_admin(client,chat_id,bot_id)
    if not check_bot:
        return await message.reply_text("Please promote me to admin first so I can proceed 😊🙏")
    bot_rights = await check_permissions(client,chat_id,bot_id,"restrict")
    if not bot_rights:
        return await message.reply_text("I don't have the rights to restrict members 🚫🔒")
    check_user = await check_admin(client,chat_id,user_id)
    if not check_user:
        return await message.reply_text("You need to be an admin to use this command ⚠️🚫")
    user_rights = await check_permissions(client,chat_id,user_id,"restrict")
    if not user_rights:
        return await message.reply_text("You don't have the rights to restrict members 🚫🔒")
    
