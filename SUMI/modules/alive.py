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
from SUMI.events import register
from SUMI import telethn as tbot, OWNER_ID, OWNER_NAME, COTB, REPOSITORY, GROUP_ALIVE_PIC
from SUMI import StartTime, dispatcher
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
    text2 = f"➢ **Mᴏsʜɪ Mᴏsʜɪ [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'ᴍ SUMI**\n"
    text2 += f"➢ **My Uptime** - `{uptime}`\n"
    text2 += f"➢ **Telethon Version** - `{version.__version__}`\n"
    text2 += f"➢ **PTB Version** - `{telegram.__version__}`\n"
    text2 += f"➢ **Pyrogram Version** - `{pyro}`\n"
    text2 += f"➢ **MY MASTER** - [{OWNER_NAME}](tg://user?id={OWNER_ID})\n"
    text2 += f"➢ **MY DEVELOPER** - [ᏆՏᎻᏆᏦᏦᏆ ᎪᏦᎪᏴᎪΝᎬ](https://t.me/ishikki_akabane)"
    BUTTON = [[Button.url("Support Chat", "https://t.me/{SUPPORT_CHAT}"), Button.url("Updates", "https://t.me/{UPDATE_CHANNEL}")]]
    on = await tbot.send_file(yes.chat_id, file="{GROUP_ALIVE_PIC}",caption=text2, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    text3 = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}),\nMy source codes are now public, you can use them for creating your own bot\nClick The Button Below To Get My Repo**"
    BUTTON = [[Button.url("Source CODE", "{REPOSITORY}"), Button.url("DEVELOPER", "https://t.me/{COTB}")]]
    await tbot.send_file(event.chat_id, file="https://telegra.ph/file/5a07ded9ebce5b693c4ff.jpg", caption=text3, buttons=BUTTON)
