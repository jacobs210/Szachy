from tkinter import *
from  board_setup import board, sboard
from  piece_setup import pieces

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
        try:
            piece = lclick.occupant
            x, y = tocor(str(square))
            lclick.occupant.to(square)
            canvas.moveto(opieces.get(piece), x, y)
        except Exception:
            pass
        square.clicked = False
        lclick.clicked = False
        print(list(map(str, pieces)))

def tocor(square):
    x = square[0]
    y = square[1]
    xlist = ["A", "B", "C", "D", "E", "F", "G", "H"]
    ylist = ["8", "7", "6", "5", "4", "3", "2", "1"]
    x = xlist.index(x)
    y = ylist.index(y)
    x *= 79
    y *= 79
    x += 32
    y += 32
    return x, y


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

canvas = Canvas(root, width=691, height=691, bg='white')
canvas.pack(anchor="center", expand=True)
canvas.create_image((0, 0),
    image=boardp,
    anchor='nw'
)
lpieces = list()
for x in range(1,9):
    lpieces.append(canvas.create_image(
       tocor(f"{chr(x+64)}2"),
        image=wpawn,
        anchor = 'nw'
    ))
lpieces.append(canvas.create_image(tocor("A1"),image=wrook,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("H1"),image=wrook,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("B1"),image=wknight,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("G1"),image=wknight,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("C1"),image=wbishop,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("F1"),image=wbishop,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("D1"),image=wqueen,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("E1"),image=wking,anchor = 'nw'))
for x in range(1,9):
    lpieces.append(canvas.create_image(
       tocor(f"{chr(x+64)}7"),
        image=bpawn,
        anchor = 'nw'
    ))
lpieces.append(canvas.create_image(tocor("A8"),image=brook,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("H8"),image=brook,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("B8"),image=bknight,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("G8"),image=bknight,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("C8"),image=bbishop,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("F8"),image=bbishop,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("D8"),image=bqueen,anchor = 'nw'))
lpieces.append(canvas.create_image(tocor("E8"),image=bking,anchor = 'nw'))
opieces = dict()
for i, x in enumerate(pieces):
    opieces[x] = lpieces[i]
canvas.bind("<Button 1>", getsquare)

root.mainloop()
