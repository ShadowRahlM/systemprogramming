# name = 'mary'
# password = 'swordfish'
# if name == 'mary':
#     print('Hello,Mary!')
#     if password == 'swordfish':
#         print('Access granted')
#     else:
#         print("Acess denied,password wrong")
# else:
#     print('none')



# name = ''
# while True:
#     print("please type your name:\n")
#     name = input()
#     if name == 'your name':
#         break

# print("thank you")

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')

# total = 0
# while total < 101:
#     print(total)
#     total += 2


for _ in range(1,11):
    print(_ ,sep=',')

num = 1
while True:
    if num > 10:
        break
    else:
        print(num,end='.')
        num += 1