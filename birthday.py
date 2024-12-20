bds = {'Maclaren':'June 2009','Doomsday':'January 2008','Darkmayhem':'Apirl 2018','LordFreiza':'September 2017'}

while True:
    name = input("Enter alias to check bd:(blank to quit),\n")
    if name == '':
        break
    if name in bds:
        print(f"{bds[name]} is birthday of {name},\n")

    else:
        print(f'{name} no info of  birthday in database')
        print('what is their bd')
        bd = input()
        bds[name]=bd
        print("database updated")
