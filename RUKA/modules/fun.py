"""
This whole module is created by ishikki akabane, dont kang, please give credits. As a developer, you should always give respect to others hardwork in coding.
Thankyou :) , have code-full day for you.
"""
import time

from RUKA import dp, OWNER_ID, BLUE_URL
from RUKA.helpers.extra import mention
from RUKA.helpers.requests import bluerequest

from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


"""
    slap_lines = [
        f"{user1} just slapped {user2} with a wet noodle! It's super effective!",
        f"{user1} gave {user2} a gentle slap. They're probably reconsidering their life choices now.",
        f"{user1} delivered a powerful slap to {user2}'s face. The crowd goes wild!",
        f"{user1} slapped {user2} so hard, their ancestors felt it!",
        f"{user1} playfully slapped {user2} on the cheek. Friendship level: ouch!",
        f"{user1} unleashed a mighty slap on {user2}! The shockwaves could be felt for miles.",
    ]
"""

async def slap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat


    reply = message.reply_to_message
    if not reply:
        await message.reply_text("can i slap you please :)")
        return

    attacker = update.effective_user # user who is slapping
    defender = reply.from_user # user who is going to get slapped
    
    if attacker.id == defender.id: # same persons
        await message.reply_text("You want to slap yourself ?")
        return
    elif defender.id == bot.id: # slaping the bot
        try:
            permissions = ChatPermissions(can_send_messages=False)
            await bot.restrict_chat_member(
                chat.id,
                attacker.id,
                permissions,
                until_date=time.time() + 60
            )
            await message.reply_text("I will mute you for slapping me you perve")
            return
        except:
            await message.reply_text("stop slapping me just because i cant mute")
            return
    elif defender.id == OWNER_ID:
        await message.reply_text("bruh, i cant slap my love :/")
        return
    else:
        url = BLUE_URL + "/slap"
        response = await bluerequest(url)
        user1 = mention(attacker.id, attacker.first_name, mention=True)
        user2 = mention(defender.id, defender.first_name, mention=True)
        await message.reply_animation(response["msg"], caption=f"{user1} slapped {user2} so hard, their ancestors felt it", parse_mode=ParseMode.MARKDOWN)


async def kiss(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat


    reply = message.reply_to_message
    if not reply:
        await message.reply_text("can i kiss you please :)")
        return

    attacker = update.effective_user # user who is kissing
    defender = reply.from_user # user who is going to get kissed
    
    if attacker.id == defender.id: # same persons
        await message.reply_text("You want to kiss yourself ?")
        return
    
    else:
        url = BLUE_URL + "/kiss"
        response = await bluerequest(url)
        user1 = mention(attacker.id, attacker.first_name, mention=True)
        user2 = mention(defender.id, defender.first_name, mention=True)
        await message.reply_animation(response["msg"], caption=f"{user1} kissed {user2} so hard that everyone is looking at them")



dp.add_handler(CommandHandler("slap", slap, block=False))
dp.add_handler(CommandHandler("kiss", kiss, block=False))