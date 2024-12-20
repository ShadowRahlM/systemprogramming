#! /usr/bin/python3.12
import re


# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)


# x = 'spam'

# while x:
#     print(x, end=' ')
#     x = x[1:] # += results into increament which the undesired effect here


# x = 10
# while x:
#     x -= 1
#     if x % 2 != 0: continue
#     print(x ,end=' ')


# y = 5

# x = y // 2


# while x > 1:
#     if y % x == 0:
#         print(y, 'has factor', x)
#         break
#     x -= 1
# else:
#     print(y ,'is prime')


# items = ["aaa", 111, (4, 5), 2.01]
# tests = [(4, 5), 2.01,'aa']


# for key in tests:

#     if key in items:

#         print(key, "was found")
#     else:
#         print(key, "not found!")

# couped = [5,3545,464,64,64,4,543,464,54,64,654,64,6878,7*68*2//4,76,4+7,64,]
# current_index = 0

# for i in couped:
#     print(i ,'is at current index',current_index) #explict way to get offset and value
#     current_index +=1
# for i ,x in enumerate(couped):#implict way to get offset and value
#     result = f'{x} => is at index:{i}'
#     print(result)


# named_list=[f'{x} is at index {i}'for i,x in enumerate(couped)]#list comphression version
# print(named_list)

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
# found = False
# i = 0
# while not found and i < len(L):
#     if 2 ** X == L[i]:
#         found = True
#     else:
#         i +=1
# if found:
#     print('at index', i)
# else:
#     print(X, 'not found')

# for x in L:
#     if 2**X == x:
#         print(2**X,'was found at',L.index(x))
#         break
#     else:
#         print(X,'not found')


# if 2 ** X in L:
#     print(2 ** X, 'was found at', L.index(2 ** X))
# else:
#     print(X, 'not found')


# st = 'spam'

# for i  in st:
#     print(ord(i))

# x=0
# for i in st:x+=ord(i)
# print(x)


# x = []
# for c in st: x.append(ord(c))
# print(x)

x = 'spam'


def func():
    print(x)


# func()

import re

def find_isbn(lst):
    # Correct ISBN pattern: matches ISBN-13 format (3 digits, then x's and dashes)
    pattern = r"\b(\d{3})-(\d)-(\d{2})-(\d{6})-(\d)\b"
    
    # Search for the pattern
    result = re.search(pattern, lst)
    
    if result is None:
        return ""  # Return empty string if no ISBN is found
    
    # Extract the relevant part of the ISBN (in this case, the 4th group)
    ans = result.group(4)
    
    # Return the result (the 4th part of the ISBN)
    return ans

# Example usage
lst = "The ISBN is 978-3-16-148410-0 in the document."
print(find_isbn(lst))  # Output: 148410
print(find_isbn("123-4-12-098754-0"))
print(find_isbn("223094-AB-12-30"))
print(find_isbn("1123-4-12-098754-0"))

# import re
# def repeating_letter_a(text):
#   result = re.search(r"a.a+", text)
#   return result != None

# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True




# def spam():
#     eggs = 'spam local'
#     print(eggs)# prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)# prints 'bacon local'
#     spam()
#     print(eggs)# prints 'bacon local'




# eggs = 'global'
# bacon()
# print(eggs)# prints 'global'

# def divison(number):
#     try:
#         return 42 // number

#     except ZeroDivisionError as e:
#         print("you can't divide by zero",e,sep=',')
#         return ""


# print(type(0//1))

# print(divison(0))
# print(divison(1))
# print(divison(5))
# print(divison(8))
# print(divison(12))


import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.
try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:# Increase the number of spaces:
            indent += 1
            if indent == 20:# Change direction:
                indentIncreasing = False
        else:# Decrease the number of spaces:
            indent -=1
            if indent == 0:# Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()



import time

indent = 0  # How many spaces to indent.
indentIncreasing = True  # Whether the indentation is increasing or not.

for _ in range(100):  # A large number to keep the loop going.
    print(' ' * indent, end='')
    print('-*/+-*/+-*/+')
    time.sleep(0.1)  # Pause for 1/10 of a second.

    if indentIncreasing:  # Increase the number of spaces:
        indent += 1
        if indent == 20:  # Change direction:
            indentIncreasing = False
    else:  # Decrease the number of spaces:
        indent -= 1
        if indent == 0:  # Change direction:
            indentIncreasing = True
