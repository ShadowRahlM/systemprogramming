#!/usr/bin/python3.12

import os
import shutil
import sys

source_folder = '/media/kali/Doomsday/tools'
dst_folder = '/media/kali/Doomsday/sorted'


def organize_files(source_folder, dst_folder):
    """
    Organizes files from the source folder into categorized folders in the destination folder
    based on their file extensions.
    """
    # Define the file types and their respective extensions
    file_types = {
        'image': ['jpg', 'png', 'gif'],
        'document': ['pdf', 'docx', 'txt'],
        'video': ['mp4', 'avi', 'mkv', 'mov']
    }
    
    # Walk through the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_extension = file_extension[1:].lower()  # Remove the dot and convert to lowercase
            
            # Determine the category of the file based on its extension
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination_path = os.path.join(dst_folder, category)
                    
                    # Create the category folder if it doesn't exist
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)
                    
                    # Move the file to the appropriate category folder
                    file_source = os.path.join(root, file)
                    file_destination = os.path.join(destination_path, file)
                    shutil.move(file_source, file_destination)
                    break  # Break out of the inner loop once the file is categorized


if __name__ == '__main__':
    organize_files(source_folder, dst_folder)
