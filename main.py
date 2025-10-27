from classes import *
from setup import *
from moves import *

Piece(0, "Pawn", Square(2, 4))
print(list(map(str, king(Piece(0, "Pawn", Square(1, 4))))))

