#!/usr/bin/python3.13

import re
pattern = r'Bat(wo)+.*'

text = 'The Adenture of Batwowo_man Batman'
result= re.search(pattern,text)
print(result.group())



pattern = r'([A-Z]+a){3,}'
text = 'HaHaHaCaCaCaSbSbbSTaTaDaDaDab'
query = re.search(pattern,text)
print(query.group())


pattern = r'\d{3}-\d{3}-\d{4}'
text = 'Cell: 415-555-9999 Work: 212-555-0000'
query = re.findall(pattern,text)
print(query)



pattern = r'\d+\s\w+'
text = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
result = re.findall(pattern,text)
print(result)