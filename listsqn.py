
#! /usr/bin env python3.13
import sys

items = ['fruits','apples','tofu','bananas','cars','Mclaren','Range_Rover']


def list_to_string(lst):
    if not lst:# check for empty list
        return ''
    if len(lst) == 1:#Handle single-item list
        return str(lst[0])
    
    #join all items except the last one with comma and space
    all_bt = ','.join(map(str,lst[:-1]))
    #append the last item with 'and'
    result = f" {all_bt} and {lst[-1]}"
    return result


value = list_to_string(items)
print(value)    
    