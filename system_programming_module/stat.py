#!/usr/bin/python3.12

import os
import stat

def print_stat_info(path):
    """
    Prints various file status information for the given path.

    Args:
        path (str): The file or directory path to get status information.
    """
    try:
        stat_info = os.stat(path)

        # Print the full stat information
        print("Stat Info:", stat_info)

        # Check if the path is a directory
        if stat.S_ISDIR(stat_info.st_mode):
            print(f"{path} is a directory")
        else:
            print(f"{path} is not a directory")

        # Print the last modification time
        print(f"Last modification time of {path}: {stat_info.st_mtime}")

        # Print the user ID of the file owner
        print(f"User ID of the file owner of {path}: {stat_info.st_uid}")

        # Check if the path is a regular file
        if stat.S_ISREG(stat_info.st_mode):
            print(f"{path} is a regular file")
        else:
            print(f"{path} is not a regular file")

    except FileNotFoundError:
        print(f"The path {path} does not exist.")
    except PermissionError:
        print(f"Permission denied for the path {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Example usage:
    path = '/media/kali/Doomsday'
    print_stat_info(path)
