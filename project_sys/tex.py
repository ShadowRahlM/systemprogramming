import os 
import datetime as dt

dir1 = os.getcwd()
dir  = os.listdir(dir1)
for file in dir:
    if not os.path.exists('config_.py'):
        cwd = os.chdir('project_sys')
        cwd = os.getcwd()
        print(cwd)
else:
    timestamp =  os.path.getmtime('config_.py')
    timestamp2 =  os.path.getctime('config_.py')
    timestamp3 =  os.path.getatime('config_.py')

    print(dt.datetime.fromtimestamp(timestamp),'\n',dt.datetime.fromtimestamp(timestamp2),'\n',dt.datetime.fromtimestamp(timestamp3))

