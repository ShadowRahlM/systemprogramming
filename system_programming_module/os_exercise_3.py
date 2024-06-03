#! /usr/bin/python3.12

import os

def file_exists(file):
    search  = file
    file_path = '/media/kali/Doomsday/tools'
    for files in os.walk(file_path):
        if search in files:
            return True
        else:
            return False
    
    
    
    
    
if __name__ == "__main__":
    print(file_exists())
    