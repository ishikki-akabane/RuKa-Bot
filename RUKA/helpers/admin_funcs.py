from functools import wraps

from telegram import Update
from telegram.ext import ContextTypes


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
            if chat.type == "private":
                f
            
            # Check if the user is an admin with the specified permission
            if user and getattr(user, permission, False):
                return func(update, context, *args, **kwargs)
            else:
                if permission == "can_add_web_page_previews":
                    message = "Sorry, you're not allowed to share links in this group. Looks like someone's still using AOL dial-up!"
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
                    message = "Sorry, you don't have permission to perform this action. Looks like someone's stuck in the kiddie pool!"
                    
                update.message.reply_text(message)
                
        return wrapper
    return decorator
