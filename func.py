from classes import Square
def sqr(val):
    return Square(val[0], val[1:])
from piece_setup import whites, blacks, pieces
from board_setup import board
from captures import capture
from moves import move
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
def ppieces(square):
    white = list()
    black = list()
    for x in pieces:
        if square in move(x):
            if x.color == "White":
                white.append(x)
            if x.color == "Black":
                black.append(x)
    return white, black
def notation(piece, square, pos):
    if len(pos) == 1:
        pass

