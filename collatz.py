# def collatz(number):
#     if number % 2 == 0:
#         result =  number // 2
#         print(result)
#         return result
#     else:
#         result = 3 * number + 1
#         print(result)
#         return result



# try:
#     user_input = int(input("Enter a number:"))
#     while user_input != 1:# continue until the result becomes one    
#         user_input = collatz(user_input)  # Update user_input with the result from collatz
        
# except ValueError as e:
#     print("Invalid input! Please enter an integer.")
# except KeyboardInterrupt:
#     print("\nProcess interrupted by user. Exiting...")



# catnames = []
# while True:
#     print('Enter the name of cat' + str(len(catnames) + 1) +'(Or enter nothing to stop.):')
#     name = input()
#     if name == '':         
#         break     
#     catnames.append(name)
# print('the cats names are:')
# for name in catnames:    
#     print(" " + name )
 


spam = [2, 5, 3.14, 1, -7]
# print(sorted(spam))
spam.sort()
print(spam)

import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
print(messages[random.randint(0, len(messages)-1)])


import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)