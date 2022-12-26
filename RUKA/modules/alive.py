import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from RUKA.events import register
from RUKA import telethn as tbot
from RUKA import OWNER_ID, OWNER_NAME, COTB, GROUP_ALIVE_PIC, BOT_NAME
from RUKA import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    text2 = f"➢ **Mᴏsʜɪ Mᴏsʜɪ [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'ᴍ {BOT_NAME}**\n"
    text2 += f"➢ **My Uptime** - `{uptime}`\n"
    text2 += f"➢ **Telethon Version** - `{version.__version__}`\n"
    text2 += f"➢ **PTB Version** - `{telegram.__version__}`\n"
    text2 += f"➢ **Pyrogram Version** - `{pyro}`\n"
    text2 += f"➢ **MY MASTER** - [{OWNER_NAME}](tg://user?id={OWNER_ID})\n"
    text2 += f"➢ **MY DEVELOPER** - [ᏆՏᎻᏆᏦᏦᏆ ᎪᏦᎪᏴᎪΝᎬ](https://t.me/ishikki_akabane)"
    BUTTON = [[Button.url("Support Chat", f"https://t.me/{SUPPORT_CHAT}"), Button.url("Updates", f"https://t.me/{UPDATE_CHANNEL}")]]
    on = await tbot.send_file(yes.chat_id, file=GROUP_ALIVE_PIC,caption=text2, buttons=BUTTON)

