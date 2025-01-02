#! /usr/bin/env python3.13

import pyperclip as p

text  = p.paste()

line = text.split('\n')
    
for x in range(len(line)):# loop through all indexes in the "lines"     
    line[x] = "* " + line[x] # add star to each string in "lines" list
    text = '\n'.join(line)
    
p.copy(text)


