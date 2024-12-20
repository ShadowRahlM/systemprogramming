#! /usr/bin/python3.12

import os 



def walk_path(cwd):

    for root ,dirs,files in os.walk(cwd):
        print(root,dirs,files)
    
    

def change_wd(dir_path): 
    os.chdir(dir_path)
    print(os.listdir(dir_path))



def env_var():
    result = os.environ.items()


if __name__ == '__main__':
    #walk_path('/root')
    #change_wd('/boot')
    env_var()