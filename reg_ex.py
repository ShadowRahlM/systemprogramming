#!/usr/bin/python3.13

import re
pattern = r'Bat(wo)+.[a-z . A-Z]*'

text = 'The Adenture of Batwowo_man Batman'
result= re.search(pattern,text)
print(result.group())
