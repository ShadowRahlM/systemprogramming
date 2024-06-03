import os, stat

stat_info = os.stat('/media/kali/Doomsday')
print(stat_info)

stat_info = os.stat('/media/kali/Doomsday')
if stat.S_ISDIR(stat_info.st_mode):
	print('Doomsday is a directory')
else:
	print('Doomsday is not a directory')
 
 
stat_info = os.stat('/media/kali/Doomsday')
print(stat_info.st_mtime)  # prints the time of last modification of the file 'Doomsday'


stat_info = os.stat('/media/kali/Doomsday')
print(stat_info.st_uid)  # prints the user ID of the file owner


stat_info = os.stat('/media/kali/Doomsday')
if stat.S_ISREG(stat_info.st_mode):
	print('Doomsday is a regular file')
else:
	print('Doomsday is not a regular file')
