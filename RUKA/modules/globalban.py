from RUKA import dp
from RUKA.helpers.errors import capture_error
from RUKA.database.sql.gban_sql import sql_savegban, sql_revertgban, sql_updategban, checkgban, gban_list

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode



@capture_error
async def gban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.effective_message
    chat_id = update.effective_chat.id
    args = context.args

    exist = await checkgban()