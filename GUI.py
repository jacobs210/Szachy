from tkinter import *
from  board_setup import board, sboard
from main import *
#import ImageTk
def show():
    for i, y in enumerate(gpieces.values()):
        xc = 79 * pieces[i].square.x - 79
        yc = 79 * pieces[i].square.y
        xp, yp = 32, 664
        xp += xc
        yp -= yc
        y.place(x = xp, y = yp)
        y.lift()
def tmove(square):
    lclick = ""
    for x in board:
        if x.clicked and x != square:
            lclick = x
    if square.clicked:
        square.clicked = False
    elif lclick == "":
        square.clicked = True
    else:
        print(lclick.occupant)
        try:
            lclick.occupant.to(square)
        except Exception:
            print("aa")
            pass
        square.clicked = False
        lclick.clicked = False
        show()
    print(list(map(str, pieces)))

def getsquare(eventorigin):
    xc = eventorigin.x
    yc = eventorigin.y
    print(xc, yc)
    xlist = ["A", "B", "C", "D", "E", "F", "G", "H"]
    ylist = ["8", "7", "6", "5", "4", "3", "2", "1"]
    if 661 > xc  > 30 and 661 > yc > 30:
        xc -= 30
        yc -= 30
        xc //= 79
        yc //= 79
        square = board[sboard.index(xlist[xc] + ylist[yc])]
        print(square)
        tmove(square)
def getpiece(i):
    print(i)

root = Tk()
root.title("Szachy")
root.geometry("691x691")
root.resizable(False, False)

boardp = PhotoImage(file="img/board.png")
wpawn = PhotoImage(file="img/wpawn.png")
bpawn = PhotoImage(file="img/bpawn.png")
wrook = PhotoImage(file="img/wrook.png")
brook = PhotoImage(file="img/brook.png")
wknight = PhotoImage(file="img/wknight.png")
bknight = PhotoImage(file="img/bknight.png")
wbishop = PhotoImage(file="img/wbishop.png")
bbishop = PhotoImage(file="img/bbishop.png")
wqueen = PhotoImage(file="img/wqueen.png")
bqueen = PhotoImage(file="img/bqueen.png")
wking = PhotoImage(file="img/wking.png")
bking = PhotoImage(file="img/bking.png")

gpieces = dict()
for x in range(1,9):
    gpieces[f"wpawn{x}"] = Label(root, image=wpawn)
gpieces["wrook1"] = Label(root, image=wrook)
gpieces["wrook2"] = Label(root, image=wrook)
gpieces["wknight1"] = Label(root, image=wknight)
gpieces["wknight2"] = Label(root, image=wknight)
gpieces["wknight2"] = Label(root, image=wknight)
gpieces["wbishop1"] = Label(root, image=wbishop)
gpieces["wbishop2"] = Label(root, image=wbishop)
gpieces["wqueen"] = Label(root, image=wqueen)
gpieces["wking"] = Label(root, image=wking)
for x in range(1,9):
    gpieces[f"bpawn{x}"] = Label(root, image=bpawn)
gpieces["brook1"] = Label(root, image=brook)
gpieces["brook2"] = Label(root, image=brook)
gpieces["bknight1"] = Label(root, image=bknight)
gpieces["bknight2"] = Label(root, image=bknight)
gpieces["bknight2"] = Label(root, image=bknight)
gpieces["bbishop1"] = Label(root, image=bbishop)
gpieces["bbishop2"] = Label(root, image=bbishop)
gpieces["bqueen"] = Label(root, image=bqueen)
gpieces["bking"] = Label(root, image=bking)
board_label = Label(root, image=boardp)
board_label.place(x = 0, y = 0)
for i, x in enumerate(gpieces.values()):
    x.bind(f"<Button{i + 2}>", getpiece(i + 2))
board_label.bind("<Button 1>", getsquare)
root.mainloop()
