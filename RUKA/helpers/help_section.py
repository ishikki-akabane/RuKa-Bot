import os
import importlib

"""
# List to store the module names
module_names = []

# Directory path where the Python files are located
directory = 'RUKA.module'

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.py'):
        # Construct the module name from the file name
        module_name = filename[:-3]

        # Load the module dynamically
        module = importlib.import_module(f'{directory}.{module_name}')

        # Get the value of the __mod_name__ variable from the module
        mod_name = getattr(module, '__mod_name__', None)

        # Append the module name to the list
        if mod_name:
            module_names.append(mod_name)


# Print the list of module names
print(">>>>>>>>>>>>>>>", module_names)
"""
#=-=============================================================================================================-=

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import importlib
import os

# Create the menu function
def create_menu():
    keyboard = []
    modules_dir = 'RUKA'

    # Get the current working directory
    current_directory = os.getcwd()

    # Iterate over the directories and files within the current directory
    for item in os.listdir(current_directory):
        # Check if the item is a directory
        if os.path.isdir(item):
            print("Directory:", item)
        # Check if the item is a file
        elif os.path.isfile(item):
            print("File:", item)

    # Iterate over the module files
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py'):
            # Construct the module name from the file name
            module_name = filename[:-3]

            # Load the module dynamically
            module = importlib.import_module(f'modules.{module_name}')

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


