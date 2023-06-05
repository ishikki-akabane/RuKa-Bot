"""
Made by Ishikki Akabane
Dont just kang or clone
Learn to value someone's hardwork, so please dont remove credits
Made with dedication and love
If you face any issues, feel free to visit @DevsLAB,
or into my DM to abuse me or for help or just to say thanks.
Thankyou if read this notice fully :), have a wonderful cody day
"""
import time
import importlib
import os

from RUKA import dp, LOGGER, StartTime, OWNER_USERNAME, SUPPORT_CHAT, BLUE_API, aiosession, OWNER_ID
from RUKA.tools.time import get_readable_time
from RUKA.modules import ALL_MODULES
#from RUKA.helpers.help_section import create_menu

from RUKA.database.sql.user_sql import sql_adduser

from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Chat, User
from telegram.constants import ParseMode


for module_name in ALL_MODULES:
    imported_module = importlib.import_module("RUKA.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    uptime = get_readable_time((time.time() - StartTime))

    if update.effective_chat.type == "private":
        await message.reply_text(
            "Im alive master, still in development.\nAlive since {}".format(uptime),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="☑ ᴀᴅᴅ RᴜKᴀ ☑",
                            url="t.me/RukaProbot?startgroup=true"
                        )
                    ],
                    [
                        InlineKeyboardButton(text="OWNER", url=f"tg://user?id={OWNER_ID}"),
                        InlineKeyboardButton(text="ABOUT", url="t.me/")
                    ],
                    [
                        InlineKeyboardButton(text="updates", url="t.me/updatesxd"),
                        InlineKeyboardButton(text="commands", url="t.me/")
                    ]
                ]
            )
        )
    else:
        await message.reply_text(
            f"I'm Alive, working since {uptime}"
        )

# Create the menu function
"""
def create_menu():
    keyboard = []
    modules_dir = 'RUKA/modules'

    # Iterate over the module files
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            # Construct the module name from the file name
            module_name = filename[:-3]

            # Load the module dynamically
            module = importlib.import_module(f'RUKA.modules.{module_name}')

            # Get the values of __mod_name__ and __help__ variables from the module
            mod_name = getattr(module, '__mod_name__', module_name)
            help_text = getattr(module, '__help__', 'No help available.')

            # Create the button with the module name as text and module_name as data
            button = InlineKeyboardButton(mod_name, callback_data=f'module:{module_name}')
            keyboard.append([button])

    # Reshape the keyboard into 3 x 6 layout
    keyboard = [keyboard[i:i + 6] for i in range(0, len(keyboard), 6)]

    # Create the InlineKeyboardMarkup with the keyboard layout
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the menu message
    return reply_markup
"""

def create_menu():
    keyboard = []
    modules_dir = 'RUKA/modules'

    # Iterate over the module files
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            # Construct the module name from the file name
            module_name = filename[:-3]

            # Load the module dynamically
            module = importlib.import_module(f'RUKA.modules.{module_name}')

            # Get the values of __mod_name__ and __help__ variables from the module
            mod_name = getattr(module, '__mod_name__', module_name)
            help_text = getattr(module, '__help__', 'No help available.')

            # Create the button with the module name as text and module_name as data
            button = {
                'text': mod_name,
                'callback_data': f'module:{module_name}'
            }
            keyboard.append([button])

    # Reshape the keyboard into 3 x 6 layout
    keyboard = [keyboard[i:i + 6] for i in range(0, len(keyboard), 6)]

    # Create the InlineKeyboardMarkup with the keyboard layout
    reply_markup = {
        'inline_keyboard': keyboard
    }

    return reply_markup


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    message = update.effective_message
    user_id = update.effective_user.id
    keyboard = create_menu()
    await message.reply_text(
        "help section",
        reply_markup=keyboard
    )


# Define the callback function for handling button presses
async def button_callback(update, context):
    query = update.callback_query
    data = query.data

    # Get the module name from the button data
    module_name = data.split(':')[1]

    # Load the module dynamically
    module = importlib.import_module(f'modules.{module_name}')

    # Get the value of the __help__ variable from the module
    help_text = getattr(module, '__help__', 'No help available.')

    # Edit the message with the help text
    await context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=help_text)


def main():

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help_cmd)
    # Register the button callback handler
    dp.add_handler(CallbackQueryHandler(button_callback))
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)

    LOGGER.info("Ruka is now deployed!!!\n----Using long polling...")
    dp.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded all modules")
    main()