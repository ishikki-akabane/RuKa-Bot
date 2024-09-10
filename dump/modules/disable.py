import asyncio

from RUKA import dp, OWNER_ID, LOGGER
from RUKA.helpers.errors import capture_error
from RUKA.helpers.formatting import get_formatted_names

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram.ext import filters as filters_module

from RUKA.database.sql.disable_sql import sql_disable, sql_enable, sql_get_alldisabled_cache


def non_async_function():
    loop = asyncio.get_event_loop()
    if loop.is_running():
        result = asyncio.create_task(sql_get_alldisabled_cache())
    else:
        result = loop.run_until_complete(sql_get_alldisabled_cache())
    return result


DISABLED_CHATS = non_async_function() # All disabled commands with their respective chats in dict form
DISABLE_CMDS = [] # All commands that can be disabled


def check_disable(chat_id, command):
    if type(command) == list:
        command = command[0]
    try:
        cmds = DISABLED_CHATS[chat_id]
    except KeyError:
        return False
    if command in cmds:
        return True
    else:
        return False


class DisableCommandHandler(CommandHandler):
    def __init__(self, command, callback, block = True, filters: filters_module.BaseFilter = None):
        super().__init__(command, callback, block=block)
        self.command = command

        if isinstance(command, list):
            for cmd in command:
                cmd = cmd.lower()
                DISABLE_CMDS.append(cmd)
        elif isinstance(command, str):
            command = command.lower()
            DISABLE_CMDS.append(command)
        else:
            LOGGER.error(f"Command: {command} is not a valid bot command")

    def check_update(self, update):
        chat_id = update.effective_chat.id
        disabled_cmd = check_disable(chat_id, self.command) # checks if it is disabled or not in that chat
        if disabled_cmd == True:
            return False
        return super().check_update(update)


@capture_error
async def disable_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = update.effective_message
    try:
        command = context.args[0] # Get the command to disable from the command arguments
    except IndexError:
        return await message.reply_text("Provide me something to disable baka")

    if command.startswith('/'):
        command = command[1:]  # Remove the leading slash if present
    if command not in DISABLE_CMDS:
        return await message.reply_text("That command cannot be disabled!")

    disabled_cmd = check_disable(chat_id, command) # checks if it is disabled or not in that chat
    if disabled_cmd == True:
        return await message.reply_text("This command is already disabled!")

    try:
        exist = DISABLED_CHATS[chat_id]
        exist.append(command)
    except KeyError:
        DISABLED_CHATS[chat_id] = [command]

    result = await sql_disable(chat_id, command)
    await message.reply_text(f"Disabled /{command} command in this group.")


@capture_error
async def enable_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = update.effective_message
    try:
        command = context.args[0] # Get the command to enable from the command arguments
    except IndexError:
        return await message.reply_text("Provide me something to enable baka")

    if command.startswith('/'):
        command = command[1:]  # Remove the leading slash if present
    if command not in DISABLE_CMDS:
        return await message.reply_text("That command cannot be enabled!")

    disabled_cmd = check_disable(chat_id, command) # checks if it is disabled or not in that chat
    if disabled_cmd == False:
        return await message.reply_text("This command is already enabled!")

 
    exist = DISABLED_CHATS[chat_id] 
    exist.remove(command) # remove command from cache memory

    result = await sql_enable(chat_id, command)
    await message.reply_text(f"Enabled /{command} command in this group.")



@capture_error
async def list_of_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = update.effective_message
    finaltext = get_formatted_names(DISABLE_CMDS)
    await message.reply_text(f"**All commands that can be disabled:**\n`{finaltext}`", parse_mode=ParseMode.MARKDOWN)


dp.add_handler(CommandHandler("commands", list_of_commands, block=False))
dp.add_handler(CommandHandler("enable", enable_command, block=False))
dp.add_handler(CommandHandler("disable", disable_command, block=False))

__mod_name__ = "disable"
__help__ = "blah blah blah disable blah"
