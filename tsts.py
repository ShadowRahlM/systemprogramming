#!/usr/bin/python3.12

import re

# Example 1: Updating wardrobe with new items
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print("Updated wardrobe:", wardrobe)

# Example 2: Using a while loop to print characters of a string
x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]  # Remove the first character each iteration

# Example 3: Using a while loop with continue and even numbers
x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue  # Skip odd numbers
    print(x, end=' ')

# Example 4: Checking if a number is prime using while-else loop
y = 5
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')

# Example 5: Checking membership in a list using for loop
items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 2.01, 'aa']

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")

# Example 6: Using enumerate to get index and value from a list
couped = [5, 3545, 464, 64, 64, 4, 543, 464, 54, 64, 654, 64, 6878, 7 * 68 * 2 // 4, 76, 4 + 7, 64]
for i, x in enumerate(couped):
    print(f'{x} is at index {i}')

# Example 7: Finding a number in a list using different methods
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# Method 1: Using a while loop
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i += 1
if found:
    print('At index', i)
else:
    print(X, 'not found')

# Method 2: Using a for loop with break
for x in L:
    if 2 ** X == x:
        print(2 ** X, 'was found at', L.index(x))
        break
else:
    print(X, 'not found')

# Method 3: Using membership check
if 2 ** X in L:
    print(2 ** X, 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# Example 8: Using ord() to get ASCII values of characters in a string
st = 'spam'
for i in st:
    print(ord(i))

# Example 9: Calculating the sum of ASCII values using a for loop
x = 0
for i in st:
    x += ord(i)
print(x)

# Example 10: Creating a list of ASCII values using list comprehension
x = [ord(c) for c in st]
print(x)

# Example 11: Function example accessing global variable
x = 'spam'

def func():
    print(x)

func()

# Example 12: Using regular expressions to find a pattern in a string
def find_isbn(lst):
    pattern = r"\b(\d{3})-(\d)-(\d{2}-(\d{6}-(\d)\b))"
    result = re.search(pattern, lst)
    if result is not None:
        return result.group(4)  # Return the 4th group if pattern matches
    return ''

print(find_isbn("123-4-12-098754-0"))
print(find_isbn("223094-AB-12-30"))
print(find_isbn("1123-4-12-098754-0"))
