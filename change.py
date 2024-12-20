#!/usr/bin/python3.12

import os

def change_and_return(dir):
    """
    Changes the current working directory to the specified directory
    and returns a recursive list of its contents.

    Parameters:
    dir (str): The directory to change to and list contents of.

    Returns:
    None
    """
    # Check if the provided directory is valid
    if not os.path.isdir(dir):
        print('Invalid folder, please provide a valid one')
        return  # Exit the function if the directory is invalid
    else:
        # Change the current working directory to the specified directory
        os.chdir(dir)
        # Recursively list all contents of the directory
        for root, dirs, files in os.walk('.'):
            for name in dirs + files:
                print(os.path.join(root, name))  # Print each item with its relative path

# Prompt the user to enter a directory
dir = input('Enter directory: ').strip()

# Change to the specified directory and list its contents
change_and_return(dir)
