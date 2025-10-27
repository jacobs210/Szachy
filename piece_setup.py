from classes import Piece, Square
from board_setup import boardMax
whites = []
blacks = []
for x in range(1, boardMax["x"] + 1):
    whites.append(Piece(0, "Pawn", Square(x, 2)))
    blacks.append(Piece(1, "Pawn", Square(x, 2)))
whites.append(Piece(0, "Rook", Square(1, 1)))
whites.append(Piece(0, "Rook", Square(8, 1)))
whites.append(Piece(0, "Knight", Square(2, 1)))
whites.append(Piece(0, "Knight", Square(7, 1)))
whites.append(Piece(0, "Bishop", Square(3, 1)))
whites.append(Piece(0, "Bishop", Square(6, 1)))
whites.append(Piece(0, "Queen", Square(4, 1)))
whites.append(Piece(0, "King", Square(5, 1)))

whites.append(Piece(1, "Rook", Square(1, 8)))
whites.append(Piece(1, "Rook", Square(8, 8)))
whites.append(Piece(1, "Knight", Square(2, 8)))
whites.append(Piece(1, "Knight", Square(7, 8)))
whites.append(Piece(1, "Bishop", Square(3, 8)))
whites.append(Piece(1, "Bishop", Square(6, 8)))
whites.append(Piece(1, "Queen", Square(4, 8)))
whites.append(Piece(1, "King", Square(5, 8)))
pieces = whites + blacks
