from RUKA import dp, OWNER_ID, LOGGER
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


DISABLE_CMDS = []

a = 2
if a == 2:
    class disablecommandhandler(CommandHandler):
        def __init__(self, command, callback, block: bool, filters: filters_module.BaseFilter = None):

            if type(command) == list:
                for comnd in command:
                    comnd = comnd.lower()
                    DISABLE_CMDS.append(comnd)
            elif type(command) == str:
                command = command.lower()
                DISABLE_CMDS.append(command)
            else:
                LOGGER.error(f"Command: {command} is not a valid bot command")

            print("done")

else:
    disablecommandhandler = CommandHandler



__mod_name__ = "chatbot"
__help__ = ""