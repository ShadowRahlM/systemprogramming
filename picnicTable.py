#! /usr/bin/env python3.13


def printpicnic(itemDict,leftWidth,rightWidth):
    print(f"PICNIC ITEMS".center(leftWidth + rightWidth,'-'))
    for k ,v in itemDict.items():
        print(k.ljust(leftWidth, '.'),f'{v}'.rjust(rightWidth))




picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printpicnic(picnicItems, 12, 5)
printpicnic(picnicItems, 20, 6)



