#! /usr/bin/python3.12

import os 

def backup_files(source,destination):
    files = []
    
    for root ,dirs in os.walk(source):
        for file in dirs:
            if os.path.isfile(file):
                dir = os.system(f'cp -rv {file} {destination}')
                files.append(dir)
                return file
            else:
                return False
            
            
            
            
if __name__ == "__main__":
    backup_files()

    
    