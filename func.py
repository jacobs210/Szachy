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
        if x.square != "Null":
            white.update(list(map(str, capture(x))))
    for x in blacks:
        if x.square != "Null":
            black.update(list(map(str, capture(x))))
    for x in board:
        x.checked = list()
        if str(x) in white:
            x.checked.append("White")
        if str(x) in black:
            x.checked.append("Black")