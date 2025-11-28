# ishikki loves vaishnavy

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
