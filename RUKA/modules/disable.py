from RUKA import dp, OWNER_ID, LOGGER
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram.ext import filters as filters_module


DISABLE_CMDS = []

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

            print("done")
            print(DISABLE_CMDS)

    def check_update(self, update):
        chat_id = update.effective_chat.id
        #if chat_id in disabled_commands and disabled_commands[chat_id] == self.command[0]:
        #    return False
        return super().check_update(update)

    """
    class disablecommandhandler(CommandHandler):
        def __init__(self, command, callback, block = True, filters: filters_module.BaseFilter = None):

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
            print(DISABLE_CMDS)
    """

else:
    disablecommandhandler = CommandHandler



__mod_name__ = "chatbot"
__help__ = ""