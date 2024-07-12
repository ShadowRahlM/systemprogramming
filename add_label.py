#! /usr/bin/python3.12

import csv


fields = ['ItemID', 'Name', 'Description', 'Owner',
'Price', 'Condition', 'DateRegistered']


with open('../tools/source_code/Chapter2/ToolhireData/tooldesc2.csv') as td_in:
    rdr = csv.DictReader(td_in, fieldnames = fields)
    items = [item for item in rdr]
with open('tooldesc3.csv', 'w', newline='') as td_out:
    wrt = csv.DictWriter(td_out, fieldnames=fields)
    wrt.writeheader()
    wrt.writerows(items)