from RUKA import dp, OWNER_ID
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


a = 2
if a == 2:
    disablecommandhandler = CommandHandler
else:
    disablecommandhandler = CommandHandler



__mod_name__ = "chatbot"
__help__ = ""