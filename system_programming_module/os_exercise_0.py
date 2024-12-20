#!/usr/bin/python3.12

import os
import resource

def list_root_directory():
    """
    Lists and prints all files and directories in the root ('/') directory.
    """
    root_dir = '/'
    try:
        list_dir = os.listdir(root_dir)
        for file in list_dir:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{root_dir}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{root_dir}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_file_info(path):
    """
    Prints the file size, user ID, and mode for the given file path.
    
    Args:
        path (str): The path to the file.
    """
    try:
        file_info = os.stat(path)
        print(f"File size: {file_info.st_size} bytes")
        print(f"User ID: {file_info.st_uid}")
        print(f"File mode: {file_info.st_mode}")
    except FileNotFoundError:
        print("File not found. Please provide a proper path to the file.")
    except PermissionError:
        print("Permission denied to access the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

<<<<<<< HEAD
for file in list_dir:
    print(file) 
=======
def display_resource_limits():
    """
    Displays the current CPU resource limits and usage.
    """
    try:
        limits = resource.getrlimit(resource.RLIMIT_CPU)
        print(f"CPU resource limits: {limits}")

        # Setting new CPU limits (hard and soft) to 10 seconds
        resource.setrlimit(resource.RLIMIT_CPU, (10, 10))

        usage = resource.getrusage(resource.RUSAGE_SELF)
        print(f"User CPU time used: {usage.ru_utime} seconds")
    except ValueError:
        print("Invalid resource limit value.")
    except resource.error as e:
        print(f"Resource limit error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")
    list_root_directory()
>>>>>>> df5d246204fb8955de77ffb66b0532fc00a8bf1c
    
    file_path = '/media/kali/Doomsday/Automation_scripts/system_programming_module/os_exercise.py'
    get_file_info(file_path)
    
    display_resource_limits()
