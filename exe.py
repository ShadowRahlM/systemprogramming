#! /usr/bin/python3.12 

import subprocess as sp
import os 
import dpkg #type: ignore
#directory = sys.argv[1]
directory = '/media/kali/Doomsday/tools'

def cwd_and_exec(folder):
    
    #change to the folder where the package to install is 
    #cwd = os.getcwd()#this can be one way to do this 
    #os.path.join(cwd,folder)
    
    os.chdir(folder)
    if not os.path.exists(folder):
        os.makedirs(folder)
        #this will extract the contents of the .deb file to a directory
    with dpkg.DebFile(folder/'code.deb') as deb:
        deb.extract()
     
    install_dir = '/opt'
    os.path.join(folder,install_dir)
    
    sp.run(['dpkg', '-i',f'{install_dir}.dir'], check=True)
    exec = sp.run('cd ..;cp -rv .vscode /home/kali'';''exit',shell=True,)
    
    
    
    
    
    
if __name__=='__main__':
    cwd_and_exec(directory)    

