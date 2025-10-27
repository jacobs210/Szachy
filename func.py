from classes import Square
def sqr(val):
    return Square(val[0], val[1:])
from piece_setup import  whites, blacks
from board_setup import  board
from captures import capture
def checking():
    white = set()
    black = set()
    for x in whites:
        print(x)
        print(x, list(map(str, capture(x))))
        #white.update(list(map(str, capture(x))))
    for x in blacks:
        black.update(capture(x))
    for x in board:
        if x in white:
            x.checked.append("White")
        if x in black:
            x.checked.append("Black")