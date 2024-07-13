#!/usr/bin/python3.12

import os 
import datetime as dt

# Get current working directory
dir1 = os.getcwd()
dir_list = os.listdir(dir1)

# Check if 'config_.py' exists in the current directory
if not os.path.exists('config_.py'):
    # Change to 'project_sys' directory if 'config_.py' does not exist
    os.chdir('project_sys')
    cwd = os.getcwd()
    print(f"Changed directory to: {cwd}")
else:
    # Get and print the timestamps if 'config_.py' exists
    timestamp = os.path.getmtime('config_.py')
    timestamp2 = os.path.getctime('config_.py')
    timestamp3 = os.path.getatime('config_.py')

    print(f"Modification time: {dt.datetime.fromtimestamp(timestamp)}")
    print(f"Creation time: {dt.datetime.fromtimestamp(timestamp2)}")
    print(f"Access time: {dt.datetime.fromtimestamp(timestamp3)}")
