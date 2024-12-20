#!/usr/bin/python3.12

import os

def walk_path(cwd):
    """
    Walks through the directory tree rooted at cwd and prints the names of directories and files.

    Args:
        cwd (str): The current working directory path to start walking.
    """
    for root, dirs, files in os.walk(cwd):
        print("Root:", root)
        print("Directories:", dirs)
        print("Files:", files)
        print("-" * 40)

def change_wd(dir_path):
    """
    Changes the current working directory to dir_path and lists the files and directories in it.

    Args:
        dir_path (str): The directory path to change to.
    """
    try:
        os.chdir(dir_path)
        print("Changed to directory:", dir_path)
        print("Contents:", os.listdir(dir_path))
    except FileNotFoundError:
        print("Directory not found:", dir_path)
    except PermissionError:
        print("Permission denied:", dir_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def env_var():
    """
    Prints all environment variables and their values.
    """
    result = os.environ.items()
    for key, value in result:
        print(f"{key}: {value}")

if __name__ == '__main__':
    # Example usage:
    # walk_path('/root')
    # change_wd('/boot')
    env_var()
