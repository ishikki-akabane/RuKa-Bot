import asyncio

from RUKA import dp, OWNER_ID, LOGGER
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram.ext import filters as filters_module

from RUKA.database.sql.disable_sql import checkdisable, sql_disable, sql_enable, sql_get_alldisabled_cache


def non_async_function():
    loop = asyncio.get_event_loop()
    if loop.is_running():
        result = asyncio.create_task(sql_get_alldisabled_cache())
    else:
        result = loop.run_until_complete(sql_get_alldisabled_cache())
    return result


DISABLED_CHATS = non_async_function()
DISABLE_CMDS = []
print(DISABLED_CHATS)
print(DISABLE_CMDS)


def check_disable(chat_id, command):
    try:
        cmds = DISABLED_CHATS[chat_id]
    except KeyError:
        return False
    if command in cmds:
        return True
    else:
        return False


a = 2
if a == 2:
    class DisableCommandHandler(CommandHandler):
        def __init__(self, command, callback, block = True, filters: filters_module.BaseFilter = None):
            super().__init__(command, callback, block=block)
            self.command = command

            if type(command) == list:
                for comnd in command:
                    comnd = comnd.lower()
                    DISABLE_CMDS.append(comnd)
            elif type(command) == str:
                command = command.lower()
                DISABLE_CMDS.append(command)
            else:
                LOGGER.error(f"Command: {command} is not a valid bot command")

            print("d1:::", DISABLE_CMDS)

        def check_update(self, update):
            chat_id = update.effective_chat.id
            print("d1:::", self.command)
            disabled_cmd = check_disable(chat_id, self.command)
            if self.command in disabled_cmd:
                return False
            return super().check_update(update)

else:
    disablecommandhandler = CommandHandler



__mod_name__ = "chatbot"
__help__ = ""