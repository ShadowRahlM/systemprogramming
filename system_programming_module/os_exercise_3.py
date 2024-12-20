#!/usr/bin/python3.12

import os

def file_exists(file, file_path='/media/kali/Doomsday/tools'):
    """
    Checks if a file exists within a specified directory path.
    
    Args:
        file (str): The name of the file to search for.
        file_path (str): The directory path to search in. Defaults to '/media/kali/Doomsday/tools'.
    
    Returns:
        bool: True if the file exists, False otherwise.
    """
    for root, dirs, files in os.walk(file_path):
        if file in files:
            return True
    return False

if __name__ == "__main__":
    file_name = input("Enter the file name to search: ")
    if file_exists(file_name):
        print(f"The file '{file_name}' exists in the directory.")
    else:
        print(f"The file '{file_name}' does not exist in the directory.")
