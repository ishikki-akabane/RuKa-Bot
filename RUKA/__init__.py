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


import os
import sys
import logging
import time
# from MeowCore import MeowCore

# Enable Logging========================================================================================X
try:
    os.remove("logs.txt")
except OSError:
    pass

FORMAT = "[RUKA] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger("RUKA")
# TIME WATCHER==========================================================================================X

START_TIME = time.time()

# ENVIRONMENT VARIABLE==================================================================================X

from .config import CONFIG_CLASS


CONFIG = CONFIG_CLASS()


LOGGER.info("====================X======================")
LOGGER.info("|          MADE BY ISHIKKI AKABANE        |")
LOGGER.info("====================X======================")

try:
    # MEOWCORE_CLIENT = MeowCore(
    #     api_key=CONFIG.MEOW_API_TOKEN,
    #     bot_name="rukabot",
    # )
    LOGGER.info("MeowCore initialized")
    # MEOWCORE_CLIENT.load_plugins(download_dir="RUKA/plugins")
except Exception as err:
    LOGGER.info(f"MeowCore initialization failed: {err}")
