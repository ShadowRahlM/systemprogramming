#! /usr/bin/python3.12

import os
import resource


dir = os.getcwd()
list_dir = os.listdir('/')


for file in list_dir:
    print(file) 
    
    
try:
    
    path = '/media/kali/Doomsday/Automation_scripts/system_programming_module/os_exercise.py'   
    file_info = os.stat(path)
    print(f'file size is {file_info.st_size},and user id is {file_info.st_uid},plus file mode{file_info.st_mode}')
    
except FileNotFoundError as e:
    print('write proper path to file')
    
limits = resource.getrlimit(resource.RLIMIT_CPU)
print(limits)   
file_resource = resource.setrlimit(resource.RLIMIT_CPU,(10,10))
usage = resource.getrusage(resource.RUSAGE_SELF)
print(usage.ru_utime)