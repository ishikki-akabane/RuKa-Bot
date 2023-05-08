"""
This whole module is created by ishikki akabane, dont kang, please give credits. As a developer, you should always give respect to others hardwork in coding.
Thankyou :) , have code-full day for you.
"""
import time

from RUKA import dp, OWNER_ID
from RUKA.helpers.extra import mention
from RUKA.helpers.requests import bluerequest

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


baseblue_url = "https://blue-api.vercel.app"
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

    reply_text = (
        message.reply_to_message.reply_text
        if message.reply_to_message
        else message.reply_text
    )

    reply = message.reply_to_message
    if not reply:
        await message.reply_text("can i slap you please :)")
        return

    attacker = update.effective_user # user who is slapping
    defender = message.reply_to_message.from_user # user who is going to get slapped
    
    if attacker.id == defender.id: # same persons
        await message.reply_text("You want to slap yourself ?")
        return
    elif defender.id == bot.id: # slaping the bot
        await bot.restrict_chat_member(
            chat.id,
            attacker.id,
            until_date=time.time() + 60
        )
        await message.reply_text("I will mute you for slapping me you perve")
        return 
    elif defender.id == OWNER_ID:
        await message.reply_text("bruh, i cant slap my love :/")
        return
    else:
        url = baseblue_url + "/slap"
        response = await bluerequest(url)
        user1 = mention(attacker.id, attacker.first_name, mention=True)
        user2 = mention(defender.id, defender.first_name, mention=True)
        await message.reply_animation(response["msg"], caption=f"{user1} slapped {user2} so hard, their ancestors felt it", parsemode=ParseMode.MARKDOWN)


dp.add_handler(CommandHandler("slap", slap))
