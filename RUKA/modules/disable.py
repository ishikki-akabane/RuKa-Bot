import asyncio

from RUKA import dp, OWNER_ID, LOGGER
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram.ext import filters as filters_module

from RUKA.database.sql.disable_sql import checkdisable, sql_disable, sql_enable

DISABLE_CMDS = []
DISABLED_CHATS = {}


def non_async_function(chat_id):
    loop = asyncio.get_event_loop()
    if loop.is_running():
        result = asyncio.create_task(checkdisable(chat_id))
    else:
        result = loop.run_until_complete(checkdisable(chat_id))
    return result


a = 2
if a == 2:
    class DisableCommandHandler(CommandHandler):
        def __init__(self, command, callback, block = True, filters: filters_module.BaseFilter = None):
            super().__init__(command, callback, block=block)

            if type(command) == list:
                for comnd in command:
                    comnd = comnd.lower()
                    DISABLE_CMDS.append(comnd)
            elif type(command) == str:
                command = command.lower()
                DISABLE_CMDS.append(command)
            else:
                LOGGER.error(f"Command: {command} is not a valid bot command")

            print(DISABLE_CMDS)

        def check_update(self, update):
            chat_id = update.effective_chat.id
            disabled_cmd = non_async_function(chat_id)
            print(self.command[0])
            if self.command[0] in disabled_cmd:
                return False
            return super().check_update(update)


else:
    disablecommandhandler = CommandHandler



__mod_name__ = "chatbot"
__help__ = ""