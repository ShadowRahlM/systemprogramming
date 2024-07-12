#! /usr/bin/python3.12

import os 
import shutil
import sys
 
source_folder = '/media/kali/Doomsday/tools'
dst_folder = '/media/kali/Doomsday/sorted'


folder = []

def organize_files(source_folder,dst_folder):
    file_types ={
    'image':['jpg','png','gif'],
    'document':['pdf','docx','txt'],
    'video':['mp4','avi','mkv','mov']
}
    
    
    for root,dirs,files in os.walk(source_folder):
        for file in files:
            file_names,file_extension = os.path.splitext(file)
            file_extension = file_extension[1:].lower()
            for category,extensions in file_types.items():
                if file_extension in extensions:
                    destination_path = os.path.join(dst_folder,category)
                    if not os.path.exists(destination_path):
                        os.makedir(destination_path)
                        file_source = os.path.join(root,file)
                        file_destination = os.path.join(destination_path,file)
                        os.rename(file_source,file_destination)
                        break 
        
        #get file extension
        #file_extenstion = os.path.splitext(filename)[1][1:].lower()
        #create separate folders for each file type
        #for folder,extentions in file_types.items():
            #if file_extenstion in extentions:
                #destination_path = os.path.join(dst_folder,folder)
                #if not os.path.exists(destination_path):
                    #os.makedirs(destination_path)
            
        #shutil.move(os.path.join(source_folder,filename),destination_path)
            
            
        
        
        
        

if __name__== '__main__':
    organize_files(source_folder,dst_folder)            