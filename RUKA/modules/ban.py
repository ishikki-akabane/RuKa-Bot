from pyrogram import Client, filters
from RUKA import DEV_USERS,OWNER_ID
from RUKA.helpers.error_logger import ErrorLogger
from RUKA.helpers.admin_func import check_permissions,check_admin

async def until_date(message, time_val):   
    possible = ["m","h","d","w"]
    try:
        exact = time_val[0]
        date = time_val[1]   
    except IndexError:
        await message.reply_text("**Invalid Syntax**")
        return None    
    if time_val[1] not in possible:
        await message.reply_text("**This Type Of Time Isn't Supported.**")
        return None
    if not exact.isdigit():
        await message.reply_text("**Invalid time amount specified**")
        return None 
    exact = int(exact)
    if date == "m":
        until = datetime.now() + timedelta(minutes=exact)
    if date == "h":
       until = datetime.now() + timedelta(hours=exact)  
    if date == "d":
       until = datetime.now() + timedelta(days=exact) 
    if date == "w":
       until = datetime.now() + timedelta(days=exact*7) 
    return until

@Client.on_message(filters.command(["ban","tban","unban"]))
@ErrorLogger
async def ban_cmd(client,message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot_id = (await client.get_me()).id
    bot_username = (await client.get_me()).username
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
    if message.command[0] == "ban":
        if not message.reply_to_message:
            try:
                username = message.text.split(" ")[1]
                ban_id = (await client.get_users(ban_id)).id
                ban_mention = (await client.get_users(ban_id)).mention
                reason = None
                try:
                    reason = message.text.split(" ")[2]
                except:
                    pass
                
                if ban_id == bot_id:
                    return await message.reply_text("I can't ban myself 🚫🤔")
                if ban_id == OWNER_ID or ban_id in DEV_USERS:
                    return await message.reply_text("I can't ban gods 🚫👑")
                await client.ban_chat_member(chat_id,ban_id)
                if not reason:
                    return await message.reply_text(f"Ban Triggered: User {ban_mention} has been banned by {message.from_user.mention} 🚫🔨")
                else:
                    return await message.reply_text(f"Ban Triggered: User {ban_mention} has been banned by {message.from_user.mention} 🚫🔨\nReason: {reason}")
            except:
                return await message.reply_text("Unable to detect the user. Please reply to the user to ban them. ❌🔍")
        else:
            try:
                ban_id = message.reply_to_message.from_user.id
                ban_mention = message.reply_to_message.from_user.mention
                reason = None
                try:
                    reason = message.text.split(" ")[1]
                except:
                    pass
                if ban_id == bot_id:
                    return await message.reply_text("I can't ban myself 🚫🤔")
                if ban_id == OWNER_ID or ban_id in DEV_USERS:
                    return await message.reply_text("I can't ban gods 🚫👑")
                await client.ban_chat_member(chat_id,ban_id)
                if not reason:
                    return await message.reply_text(f"Ban Triggered: User {ban_mention} has been banned by {message.from_user.mention} 🚫🔨")
                else:
                    return await message.reply_text(f"Ban Triggered: User {ban_mention} has been banned by {message.from_user.mention} 🚫🔨\nReason: {reason}")
            except:
                return await message.reply_text("Something went wrong ❌")
    elif message.command[0] == "unban":
        if not message.reply_to_message:
            try:
                username = message.text.split(" ")[1]
                ban_id = (await client.get_users(ban_id)).id
                ban_mention = (await client.get_users(ban_id)).mention
                await client.unban_chat_member(chat_id,ban_id)
                return await message.reply_text(f"Unban Triggered: User {ban_mention} has been unbanned by {message.from_user.mention} 🛠️")
            except:
                return await message.reply_text("Unable to detect the user. Please reply to the user to unban them. 🔍")
        else:
            try:
                ban_id = message.reply_to_message.from_user.id
                ban_mention = message.reply_to_message.from_user.mention
                await client.unban_chat_member(chat_id,ban_id)
                return await message.reply_text(f"Unban Triggered: User {ban_mention} has been unbanned by {message.from_user.mention} 🛠️")
            except:
                return await message.reply_text("Something went wrong ❌")
    elif message.command[0] == "tban":
        if not message.reply_to_message:
            try:
                username = message.text.split(" ")[2]
                ban_id = (await client.get_users(ban_id)).id
                ban_mention = (await client.get_users(ban_id)).mention
                reason = None
                time_val = None
                try:
                    time_val = message.text.split(" ")[1].lower()
                    reason = message.text.split(" ")[3]
                except:
                    pass
                if ban_id == bot_id:
                    return await message.reply_text("I can't ban myself 🚫🤔")
                if ban_id == OWNER_ID or ban_id in DEV_USERS:
                    return await message.reply_text("I can't ban gods 🚫👑")
                if not time_val:
                    return await message.reply_text("You haven't specified a valid time ⏳❗")
                await client.ban_chat_member(chat_id,
              
       
     
           



                
