#! /usr/bin/env python3.13

import pprint as p 


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

p.pprint(chess_moves)

def valid_move(chess_board, piece, color=None):
    moves = chess_board.get(piece, {})
    if isinstance(moves, dict):
        moves = moves.get(color, [])
    move = input(f"Enter move for {piece}: ")
    if move not in moves:
        print(f"Move is invalid: {move}")
        return False
    else:
        print(f"Moved to: {move}")
        return True

move = valid_move(chess_moves, 'knight', 'white')
print(f"Valid move: {move}")




def add_to_inventory(inventory, added_items):
    print(f"current inventory: {inventory}")
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragonLoot)
# print(f"Updated inventory: {inv}")
