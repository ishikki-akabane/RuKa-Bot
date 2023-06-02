import os
import importlib

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
print(module_names)
