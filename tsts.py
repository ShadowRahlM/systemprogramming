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

#couped = [5,3545,464,64,64,4,543,464,54,64,654,64,6878,7*68*2//4,76,4+7,64,]
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

x='spam'

def func():
    print(x)


# func()



def find_isbn(lst):
     pattern = r"\b(\d{3})-(\d)-(\d{2}-(\d{6}-(\d)\b))"
     result = re.search(pattern,lst)
     if result is not None:
         return ''
     ans = f"{result[4]}"
     return (ans)
    #pattern = r"\d"
    #result = re.findall(pattern,lst)
    #number_str = re.sub(r'\D','',''.join(map(str,result)))
    



print(find_isbn("123-4-12-098754-0"))
print(find_isbn("223094-AB-12-30"))
print(find_isbn("1123-4-12-098754-0"))
