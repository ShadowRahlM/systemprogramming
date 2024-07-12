import csv
from datetime import datetime

def convertDate(item):
    theDate = item[-1]
    dateObj = datetime.strptime(theDate, '%Y-%m-%d')
    dateStr = dateObj.strftime('%m/%d/%Y')
    item[-1] = dateStr
    return item

# Read the original CSV file
with open('../tools/source_code/Chapter2/ToolhireData/tooldesc.csv', 'r') as td:
    rdr = csv.reader(td)
    items = list(rdr)

# Convert dates in the items
items = [convertDate(item) for item in items]

# Write the modified items to a new CSV file
with open('tooldesc2.csv', 'w', newline='') as td:
    wrt = csv.writer(td)
    wrt.writerows(items)
