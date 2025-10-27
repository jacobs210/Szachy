from classes import Square
from setup import board, sboard, boardMax
from func import sqr
def pawn(piece):
    tmoves = []
    moves = []
    square = piece.square
    if piece.Moved:
        if piece.color == "White":
            tmoves.append(square.up())
        else:
            tmoves.append(square.down())
    else:
        if piece.color == "White":
            tmoves.append(square.up())
            tmoves.append(square.up(2))
        else:
            tmoves.append(square.down())
            tmoves.append(square.down(2))
    for x in tmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    return moves
def knight(piece):
    tmoves = []
    moves = []
    square = piece.square
    tmoves.append(sqr(square.up(2)).left())
    tmoves.append(sqr(square.up(2)).right())
    tmoves.append(sqr(square.up()).right(2))
    tmoves.append(sqr(square.up()).left(2))
    tmoves.append(sqr(square.down(2)).left())
    tmoves.append(sqr(square.down(2)).right())
    tmoves.append(sqr(square.down()).right(2))
    tmoves.append(sqr(square.down()).left(2))
    for x in tmoves:
        if x in sboard and board[sboard.index(x)].occupant == "Null":
            moves.append(board[sboard.index(x)])
    return moves
def bishop(piece):
    urmoves = []
    ulmoves = []
    drmoves = []
    dlmoves = []
    moves = []
    square = piece.square
    for x in range(1, max(boardMax.values())):
        urmoves.append(sqr(square.up(x)).right(x))
        ulmoves.append(sqr(square.up(x)).left(x))
        drmoves.append(sqr(square.down(x)).right(x))
        dlmoves.append(sqr(square.down(x)).left(x))
    for x in urmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in ulmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in drmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in dlmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    return moves
def rook(piece):
    square = piece.square
    umoves = []
    dmoves = []
    rmoves = []
    lmoves = []
    moves = []
    for x in range(1, max(boardMax.values())):
        umoves.append(square.up(x))
        dmoves.append(square.down(x))
        rmoves.append(square.right(x))
        lmoves.append(square.left(x))
    for x in umoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in dmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in rmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    for x in lmoves:
        if x in sboard:
            if board[sboard.index(x)].occupant == "Null":
                moves.append(board[sboard.index(x)])
            else:
                break
    return moves
def queen(piece):
    return bishop(piece).extend(rook(piece))
def king(piece):
    tmoves = []
    moves = []
    square = piece.square
    tmoves.append(square.up())
    tmoves.append(square.down())
    tmoves.append(square.left())
    tmoves.append(square.right())
    tmoves.append(sqr(square.up()).right())
    tmoves.append(sqr(square.up()).left())
    tmoves.append(sqr(square.down()).right())
    tmoves.append(sqr(square.down()).left())
    for x in tmoves:
        if x in sboard and board[sboard.index(x)].occupant == "Null" and not square.checked:
            moves.append(board[sboard.index(x)])
    return moves