# Ruka-Bot - Telegram Group Management Bot
# Copyright (C) 2023-2025 Ishikki Akabane <https://github.com/ishikki-akabane>
#
# This file is part of Ruka-Bot.
#
# Ruka-Bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ruka-Bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Ruka-Bot.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client

from RUKA import LOGGER, CONFIG


async def notify_online(client: Client) -> None:
    LOGGER.info("[RUKA]: BOOTING.......")
    if not CONFIG.SUPPORT_CHAT_ID:
        return
    try:
        await client.send_message(CONFIG.SUPPORT_CHAT_ID, "Client Host is Online!")
    except Exception as err:
        LOGGER.info(f"Bot wasn't able to send message in your log Group\n\nERROR: {err}")


class Bot(Client):
    def __init__(self) -> None:
        super().__init__(
            "rukabot",
            api_id=CONFIG.API_ID,
            api_hash=CONFIG.API_HASH,
            bot_token=CONFIG.BOT_TOKEN,
            plugins={"root": "RUKA.plugins"},
        )

    async def start(self, *args, **kwargs):
        await super().start(*args, **kwargs)
        LOGGER.info("Bot Online")
        await notify_online(self)

    async def stop(self, *args, **kwargs):
        await super().stop(*args, **kwargs)
        LOGGER.info("Stopped Services")


if __name__ == "__main__":
    Bot().run()
