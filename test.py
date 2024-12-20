#!/usr/bin/python3.12

import os
import glob
import shutil as sh
import time
from os import path

# List all files and directories in the current directory
print("List of files and directories in the current directory:")
print(os.listdir())

# Use glob to find all files and directories in the current directory
print("\nUsing glob to list all files and directories:")
print(glob.glob("*"))

# Example of copying a directory tree, ignoring .pyc files
# Uncomment the line below if you want to copy the 'bitwise' directory
# sh.copytree('../bitwise', '../sorted_backup', ignore=sh.ignore_patterns('*.pyc'))

# Get and print the last modification time of the current directory
mod_time = os.path.getmtime(".")
print("\nLast modification time of the current directory (in seconds since epoch):")
print(mod_time)

# Get and print the absolute path of 'bitwise'
abs_path_bitwise = os.path.abspath("bitwise")
print("\nAbsolute path of 'bitwise':")
print(abs_path_bitwise)

# Get and print the real path or relative path of 'one_click_install'
real_path_one_click = os.path.realpath("../one_click_install")
print("\nReal path of '../one_click_install':")
print(real_path_one_click)

# Split the path into root and remaining part
root, check = os.path.split("bitwise")
print("\nRoot and remaining part after splitting 'bitwise':")
print(root, check)

# Split the file name into name and extension
name, ext = os.path.splitext("bits.py")
print("\nName and extension of 'bits.py':")
print(name, ext)

# Get and print the directory and filename from a given path
folder, filename = os.path.split(path.abspath("../tools/exe.py"))
print("\nDirectory and filename of '../tools/exe.py':")
print(folder, filename)

# Join the folder and filename to form a complete path
full_path = path.join(folder, filename)
print("\nFull path by joining folder and filename:")
print(full_path)

# Convert a given time in seconds since epoch to a human-readable format
formatted_time = time.strftime("%Y/%m/%d/%H:%M", time.localtime(1717785491.5063586))
print("\nFormatted time from given epoch seconds:")
print(formatted_time)

# Copy 'bits.py' to '../sorted/' directory
sh.copy("bits.py", "../sorted/")

# Check if a file is a symbolic link
is_link = path.islink("bit.py")
print("\nIs 'bit.py' a symbolic link?:")
print(is_link)

# Get and print the creation time of the copied file
creation_time = path.getctime("../sorted/bits.py")
formatted_creation_time = time.strftime("%y/%m/%d-%H:%M", time.localtime(creation_time))
print("\nFormatted creation time of '../sorted/bits.py':")
print(formatted_creation_time)
