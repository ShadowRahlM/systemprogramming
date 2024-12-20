#!/usr/bin/python3.12
import os

def list_all_files(folder):
    """
    Recursively lists all files and directories in the specified folder.

    Args:
        folder (str): The path to the folder to be listed.

    Returns:
        list: A list of tuples, each containing the root directory, directories, and files.
    """
    all_files = []
    try:
        for root, dirs, files in os.walk(folder):
            all_files.append((root, dirs, files))
    except Exception as e:
        print(f"An error occurred: {e}")
    return all_files

if __name__ == '__main__':
    folder_path = '/media/kali/Doomsday/'
    files_and_dirs = list_all_files(folder_path)
    for root, dirs, files in files_and_dirs:
        print(f"Root: {root}")
        print(f"Directories: {dirs}")
        print(f"Files: {files}")
        print("-" * 40)
