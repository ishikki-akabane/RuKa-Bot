

import asyncio
import uvloop
from pyrogram import Client
import traceback
import requests

from . import LOGGER, TOKEN, API_HASH, API_ID, SUPPORT_CHAT

class Bot(Client):
    def __init__(self):
        super().__init__(
            "RUKAPROBOT",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            plugins={"root": "RUKA.plugins"},
        )
    
    async def start(self):
        await super().start()
        me = await self.get_me()  # Fetch bot information to confirm successful start
        LOGGER.info(f"{me.first_name} (@{me.username}) started successfully.")

        # Notify the support chat that the bot has started
        try:
            await self.send_message(SUPPORT_CHAT, f"{me.first_name} has started successfully!")
        except Exception as e:
            LOGGER.error(f"Failed to send start message to support chat: {e}")
            LOGGER.debug(traceback.format_exc())

    async def stop(self):
        await super().stop()

if __name__ == "__main__":
    uvloop.install()
    Bot().run()
