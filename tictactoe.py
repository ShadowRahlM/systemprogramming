#! /usr/bin/ env python3.13
import pprint

theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


# theBoard = {
#     "top-L": "O",
#     "top-M": "O",
#     "top-R": "O",
#     "mid-L": "X",
#     "mid-M": "X",
#     "mid-R": " ",
#     "low-L": " ",
#     "low-M": " ",
#     "low-R": "X",
# }
# st = pprint.pformat(theBoard)
# print(st)


def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


printBoard(theBoard)





