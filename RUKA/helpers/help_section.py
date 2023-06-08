from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import importlib
import os

# Create the menu function
# By @ishikki_akabane
async def create_menu():
    keyboard = []
    modules_dir = 'RUKA/modules'
    modules_show_name = []
    modules_cll_name = {}

    # Iterate over the module files
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            # Construct the module name from the file name
            module_name = filename[:-3]

            # Load the module dynamically
            module = importlib.import_module(f'RUKA.modules.{module_name}')
            # Get the values of __mod_name__ and __help__ variables from the module
            try:
                mod_name = getattr(module, '__mod_name__')
                help_text = getattr(module, '__help__',)
            except Exception as e:
                print(e)
                pass
            try:
                modules_name.append(mod_name)
                modules_cll_name[mod_name] = module_name
            except:
                pass
    
    print(">>>", modules_show_name)
    print(">>>", modules_cll_name)
    modules_show_name.sort() # arranging them in alphabatical way
    for mod in modules_show_name:
        # Create the button with the module name as text and module_name as data
        button = InlineKeyboardButton(text=mod, callback_data=f'module={modules_cll_name[mod]}')
        keyboard.append(button)

    # Reshape the keyboard into 3 x 6 layout
    keyboard = [keyboard[i:i + 3] for i in range(0, len(keyboard), 3)]
    keyboard.append([InlineKeyboardButton(text="Back", callback_data='ishikki=back_btn')])
    # Create the InlineKeyboardMarkup with the keyboard layout
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the menu message
    return reply_markup