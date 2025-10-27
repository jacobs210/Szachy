class Square:
    def __init__(self, x, y):
        self.x = x if isinstance(x, int) else ord(x) - 64
        self.y = y
        self.occupant = "Null"
        self.checked = False
    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False
    def __str__(self):
        return f"{chr(self.x + 64)}{self.y}"
    def up(self, val = 1):
        return f"{chr(self.x + 64)}{self.y + val}"
    def down(self, val = 1):
        return f"{chr(self.x + 64)}{self.y - val}"
    def right(self, val = 1):
        return f"{chr(self.x + 64 + val)}{self.y }"
    def left(self, val = 1):
        return f"{chr(self.x + 64 - val)}{self.y}"
from setup import board
class Piece:
    def __init__(self, color, typ, square):
        if color in ["White", "Black"]:
            self.color = color
        elif color in [0, 1]:
            self.color = ["White", "Black"][color]
        self.typ = typ
        self.square = board[board.index(square)]
        self.square.occupant = self
        self.Moved = False


