from tkinter import *

import piece_setup
from  board_setup import board, sboard
from main import *
csquare = None
psquare = None
def tmove(square):
    global csquare, psquare
    psquare = csquare
    csquare = square
    try:
        if psquare != csquare and psquare.occupant != "Null":
            print(psquare, csquare, psquare.occupant)
            psquare.occupant.move(csquare)
            csquare = None
            psquare = None
    except:
        pass
def getsquare(eventorigin):
    xc = eventorigin.x
    yc = eventorigin.y
    xlist = ["A", "B", "C", "D", "E", "F", "G", "H"]
    ylist = ["8", "7", "6", "5", "4", "3", "2", "1"]
    if 661 > xc  > 30 and 661 > yc > 30:
        xc -= 30
        yc -= 30
        xc //= 79
        yc //= 79
    square = board[sboard.index(xlist[xc] + ylist[yc])]
    tmove(square)
root = Tk()
root.title("Szachy")
boardp = PhotoImage(file="img/board.png")
board_label = Label(root, image=boardp)
board_label.pack()
root.bind("<Button 1>", getsquare)
root.mainloop()
