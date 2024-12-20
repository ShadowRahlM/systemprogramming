import os 
import datetime
def file_creation(file):
    with open(file,'w') as f:
        pass

    timestamp = datetime.datetime.fromtimestamp(file)

    return os.path.abspath(timestamp)



print(file_creation("niggas"))