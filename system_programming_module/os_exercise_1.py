#! /usr/bin python3.12
import os

def list_all_files(folder):
    file = []
    dir = os.walk(folder)
    for files in dir:
        #check_dir = os.path.isdir(files
        file.append(files)
    return file    
        
        
        
        
if __name__=='__main__':
    print(list_all_files('/media/kali/Doomsday/'))
    