#!/usr/bin/python3.12

import subprocess as sp
import os

def cwd_and_exec(folder):
    # Change directory to the specified folder
    os.chdir(folder)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Assuming 'code.deb' is located in the folder, extract its contents
    # Adjust this part based on the correct location and extraction method
    deb_file = os.path.join(folder, 'code.deb')
    if os.path.isfile(deb_file):
        sp.run(['dpkg', '-x', deb_file, folder])
    
    # Installation directory path
    install_dir = '/opt'
    install_path = os.path.join(folder, install_dir)
    
    # Install the package using dpkg
    sp.run(['dpkg', '-i', install_path], check=True)
    
    # Example of copying '.vscode' directory to '/home/kali'
    sp.run(['cp', '-rv', '.vscode', '/home/kali'])

if __name__ == '__main__':
    directory = '/media/kali/Doomsday/tools'  # Replace with your actual directory
    cwd_and_exec(directory)
