from classes import Square
boardMax = {"x": 8, "y": 8}
board = [Square(x, y) for x in range(1, boardMax["x"] + 1) for y in range(1, boardMax["y"] + 1)]
sboard = list(map(str, board))


