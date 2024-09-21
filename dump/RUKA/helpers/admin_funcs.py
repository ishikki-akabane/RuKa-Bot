from functools import wraps
import random

from telegram import Update
from telegram.ext import ContextTypes

"""FUN Lines""" # designed by ishikki akabane(t.me/ishikki_akabane)
funny_lines = {
    "can_add_web_page_previews": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ꜱʜᴀʀᴇ ʟɪɴᴋꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ. ʟᴏᴏᴋꜱ ʟɪᴋᴇ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ɴᴏᴛ ʀᴇᴀᴅʏ ꜰᴏʀ ᴛʜᴇ ᴡᴏʀʟᴅ ᴡɪᴅᴇ ᴡᴇʙ ʏᴇᴛ!"
    ],
    "can_send_polls": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ꜱᴛᴀʀᴛ ᴀ ᴘᴏʟʟ. ɪ ɢᴜᴇꜱꜱ ʏᴏᴜʀ ᴏᴘɪɴɪᴏɴꜱ ᴀʀᴇɴ'ᴛ ᴛʜᴀᴛ ᴘᴏᴘᴜʟᴀʀ!"
    ],
    "can_change_info": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ᴇᴅɪᴛ ɢʀᴏᴜᴘ ɪɴꜰᴏ. ɪ ɢᴜᴇꜱꜱ ᴛʜᴇ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ꜱᴛᴀʏ ʙᴏʀɪɴɢ ꜰᴏʀ ɴᴏᴡ!"
    ],
    "can_delete_messages": [

    ],
    "can_invite_users": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴛᴏ ᴛʜɪꜱ ɢʀᴏᴜᴘ. ᴅɪᴅ ʏᴏᴜ ꜰᴏʀɢᴇᴛ ʏᴏᴜʀ ꜱᴇᴄʀᴇᴛ ʜᴀɴᴅꜱʜᴀᴋᴇ?",
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ɪɴᴠɪᴛᴇ ᴜꜱᴇʀꜱ ᴛᴏ ᴛʜɪꜱ ɢʀᴏᴜᴘ. ᴍᴀʏʙᴇ ᴛʜᴇʏ ᴊᴜꜱᴛ ᴅᴏɴ'ᴛ ʟɪᴋᴇ ʏᴏᴜ ᴇɴᴏᴜɢʜ ʏᴇᴛ!"   
    ],
    "can_restrict_members": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ ᴛᴏ ᴡɪᴇʟᴅ ᴛʜᴇ ʙᴀɴ ʜᴀᴍᴍᴇʀ. ᴅɪᴅ ʏᴏᴜ ꜰᴏʀɢᴇᴛ ʏᴏᴜʀ ꜱᴜᴘᴇʀʜᴇʀᴏ ᴄᴀᴘᴇ ᴀᴛ ʜᴏᴍᴇ?",
        "ꜱᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ ᴛᴏ ᴡɪᴇʟᴅ ᴛʜᴇ ʙᴀɴ ʜᴀᴍᴍᴇʀ. ɪᴛ'ꜱ ᴏᴋᴀʏ, ᴡᴇ'ʟʟ ʜᴀɴᴅʟᴇ ᴛʜᴇ ᴛᴏᴜɢʜ ᴅᴇᴄɪꜱɪᴏɴꜱ ꜰᴏʀ ʏᴏᴜ!"   
    ],
    "can_pin_messages": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ᴘɪɴ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ. ɪ ɢᴜᴇꜱꜱ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇꜱ ᴊᴜꜱᴛ ᴀʀᴇɴ'ᴛ ꜱᴛɪᴄᴋʏ ᴇɴᴏᴜɢʜ!",
        "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ᴘɪɴ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ. ɪ ɢᴜᴇꜱꜱ ʏᴏᴜʀ ᴊᴏᴋᴇꜱ ᴀʀᴇɴ'ᴛ ꜰᴜɴɴʏ ᴇɴᴏᴜɢʜ ᴛᴏ ꜱᴛɪᴄᴋ ᴀʀᴏᴜɴᴅ!"
    ],
    "can_promote_members": [
        "ꜱᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ ᴏꜰ ᴛʜᴇ ᴘʀᴏᴍᴏᴛɪᴏɴ. ᴍᴀʏʙᴇ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴡᴏʀᴋ ᴏɴ ʏᴏᴜʀ ʙʀᴏᴡɴ-ɴᴏꜱɪɴɢ ꜱᴋɪʟʟꜱ!",
        "ꜱᴏʀʀʏ, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ ᴏꜰ ᴛʜᴇ ᴘʀᴏᴍᴏᴛɪᴏɴ. ᴍᴀʏʙᴇ ɪꜰ ʏᴏᴜ ᴡᴇʀᴇɴ'ᴛ ᴀʟᴡᴀʏꜱ ʟᴀᴛᴇ ᴛᴏ ᴍᴇᴇᴛɪɴɢꜱ..."
    ],
    "can_manage_chat": [

    ],
    "can_manage_video_chats": [

    ]
}


def check_admin(
    permission=None,
    is_bot=False,
    is_user=False,
    is_both=True
    ):
    def decorator(func):
        @wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
            user = update.effective_user
            chat = update.effective_chat
            message = update.effective_message
            
            if is_user == True:
                # Check if the user is an admin with the specified permission
                if user and getattr(user, permission, False):
                    return func(update, context, *args, **kwargs)
                else:
                    if permission == "can_add_web_page_previews":
                        message = "Sorry, you're not allowed to share links in this group. Looks like someone's not ready for the World Wide Web yet!"
                    elif permission == "can_send_messages":
                        message = "Sorry, you're not authorized to send messages in this group. Did you forget to renew your messaging license?"
                    elif permission == "can_send_media_messages":
                        message = "Sorry, you're not authorized to send media messages in this group. Did you get lost on the way to the photography club?"
                    elif permission == "can_send_polls":
                        message = "Sorry, you don't have the right to start a poll. I guess your opinions aren't that popular!"
                    elif permission == "can_send_other_messages":
                        message = "Sorry, you're not allowed to send other types of messages in this group. Did you forget your decoder ring?"
                    elif permission == "can_add_voices":
                        message = "Sorry, you don't have the right to add voice chats to this group. Maybe you're not ready for the big leagues!"
                    elif permission == "can_change_info":
                        message = "Sorry, you don't have the right to edit group info. I guess the group name will have to stay boring for now!"
                    elif permission == "can_invite_users":
                        message = "Sorry, you don't have the right to invite users to this group. Did you forget your secret handshake?"
                    elif permission == "can_pin_messages":
                        message = "Sorry, you don't have the right to pin messages in this group. I guess your messages just aren't sticky enough!"
                    elif permission == "can_promote_members":
                        message = "Sorry, you're not worthy of the promotion. Maybe you need to work on your brown-nosing skills!"
                    elif permission == "can_restrict_members":
                        message = "Sorry, you're not worthy to wield the ban hammer. Did you forget your superhero cape at home?"
                    else:
                        message = "ꜱᴏʀʀʏ, ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ. ʟᴏᴏᴋꜱ ʟɪᴋᴇ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ꜱᴛᴜᴄᴋ ɪɴ ᴛʜᴇ ᴋɪᴅᴅɪᴇ ᴘᴏᴏʟ!"
                        
                    await message.reply_text(message)
                
        return wrapper
    return decorator
