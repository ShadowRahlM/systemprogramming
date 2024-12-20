#!/usr/bin/python3.12

import os
import shutil

def backup_files(source, destination):
    """
    Backs up files from the source directory to the destination directory.

    Args:
        source (str): The path to the source directory.
        destination (str): The path to the destination directory.
        
    Returns:
        list: A list of files that were backed up.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    files_backed_up = []

    for root, dirs, files in os.walk(source):
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination, os.path.relpath(source_file_path, source))
            destination_dir = os.path.dirname(destination_file_path)

            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            shutil.copy2(source_file_path, destination_file_path)
            files_backed_up.append(destination_file_path)
    
    return files_backed_up

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    if os.path.isdir(source_folder):
        backed_up_files = backup_files(source_folder, destination_folder)
        if backed_up_files:
            print("Files backed up successfully:")
            for file in backed_up_files:
                print(file)
        else:
            print("No files found to back up.")
    else:
        print("Invalid source directory.")
