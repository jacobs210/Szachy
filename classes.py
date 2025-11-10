class Square:
    def __init__(self, x, y):
        self.x = x if isinstance(x, int) else ord(x) - 64
        self.y = y
        self.occupant = "Null"
        self.checked = []
        self.clicked = False
    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.__key() == other.__key()
        return NotImplemented
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
class Piece:
    def __init__(self, color, typ, square):
        from board_setup import board, sboard
        if color in ["White", "Black"]:
            self.color = color
        elif color in [0, 1]:
            self.color = ["White", "Black"][color]
        self.typ = typ
        self.square = board[sboard.index(str(square))]
        self.square.occupant = self
        self.Moved = False
    def __str__(self):
        return f"{self.color} {self.typ} on {self.square}"
    def to(self, square):
        from func import checking
        from board_setup import board, sboard
        from moves import move
        from captures import capture
        from piece_setup import pieces
        checking()
        square = board[board.index(square)]
        cast = dict()
        if self.typ == "King":
            moves, cast = move(self)
        else:
            moves = move(self)

        if square.occupant == "Null" and square in moves:
            square.occupant = self
            self.square.occupant = "Null"
            self.square = square
            self.Moved = True
            return "Moving", None
        elif square.occupant != "Null" and square.occupant.color != self.color and square in capture(self):
            pieces[pieces.index(square.occupant)] = "Null"
            square.occupant.square = "Null"
            self.square.occupant = "Null"
            square.occupant = self
            self.square = square
            self.Moved = True
            return "Capturing", None
        elif square in cast.keys():
            rook = cast[square]
            square.occupant = self
            self.square.occupant = "Null"
            self.square = square
            self.Moved = True
            if str(rook.square)[0] == "A":
                board[sboard.index(square.right())].occupant = rook
            else:
                board[sboard.index(square.left())].occupant = rook
            rook.square.occupant = "Null"
            if str(rook.square)[0] == "A":
                rook.square = board[sboard.index(square.right())]
            else:
                rook.square = board[sboard.index(square.left())]
            rook.Moved = True
            return "Castling", rook

        else:
            raise Exception