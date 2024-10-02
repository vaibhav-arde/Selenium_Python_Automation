import os

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory name from the path
folder_name = os.path.dirname(script_path)

print(folder_name)