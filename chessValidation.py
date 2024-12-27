#! /usr/bin/env python3.13

chess_moves = {}


def vaild_move(chess_board, valid_m):
    for k, v in chess_board.items():
        move = input()
        # move += v.get(vaild_move,0)
        if not move in k.get(valid_m, 0):
            print(f'move is invalid:{move}')
            return False
        else:
            print(f'moved to:{move}')
    return True


def add_to_inventory(inventory, added_items):
    print(f"current inventory:{inventory}")
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragonLoot)
print(f"Updated inventory: {inv}")
