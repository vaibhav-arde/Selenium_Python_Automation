

import os

# Get the folder name of the current script
script_path = os.path.abspath(__file__)
print("script_path", script_path)

cwd= os.getcwd()
print("cwd", cwd)

folder_name = os.path.dirname(os.path.dirname(script_path))
print("folder_name", folder_name)
# Set the download path to a subfolder within the current script's folder
log_path = os.path.join(folder_name, "logs/logfile.log")
print("log_path", log_path)