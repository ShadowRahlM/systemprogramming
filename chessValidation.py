#! /usr/bin/env python3.13

chess_moves = {
    'pawn': {
        'white': [
            'forward 1', 
            'forward 2 (initial)', 
            'capture diagonally', 
            'en passant', 
            'promotion'
        ],
        'black': [
            'forward 1', 
            'forward 2 (initial)', 
            'capture diagonally', 
            'en passant', 
            'promotion'
        ]
    },
    'knight': [
        'L-shape (2 forward, 1 left/right)',
        'L-shape (2 backward, 1 left/right)',
        'L-shape (2 left, 1 forward/backward)',
        'L-shape (2 right, 1 forward/backward)'
    ],
    'bishop': [
        'diagonal (any number of squares)'
    ],
    'rook': [
        'horizontal (any number of squares)',
        'vertical (any number of squares)',
        'castling'
    ],
    'queen': [
        'horizontal (any number of squares)',
        'vertical (any number of squares)',
        'diagonal (any number of squares)'
    ],
    'king': [
        'one square in any direction',
        'castling'
    ]
}

print(chess_moves)

def valid_move(chess_board, valid_m):
    for k, v in chess_board.items():
        move = input(f"Enter move for {k}: ")
        if not move in v.get(valid_m, []):
            print(f"Move is invalid: {move}")
            return False
        else:
            print(f"Moved to: {move}")
    return True


def add_to_inventory(inventory, added_items):
    print(f"current inventory: {inventory}")
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragonLoot)
print(f"Updated inventory: {inv}")
