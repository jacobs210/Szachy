from tkinter import *
from board_setup import board, sboard
from piece_setup import pieces, whites, blacks
from func import checking, ppieces, sqr
from classes import Piece
from moves import move
from captures import capture

def tmove(square, shown = True):
    if shown:
        global clickID, lmove, var
        var = IntVar(value=0)

        lclick = ""
        for x in board:
            if x.clicked and x != square:
                lclick = x
        if square.clicked:
            square.clicked = False
            canvas.delete(clickID)
        elif lclick == "":
            square.clicked = True
            clickID = canvas.create_image(tocor(str(square)), image=clicked, anchor='nw')
        else:
            try:
                piece = lclick.occupant
                color = piece.color
                king = pieces[15] if piece.color == "White" else pieces[31]
                nColor = "Black" if king.color == "White" else "White"
                psquare = piece.square
                if lmove != piece.color:
                    x, y = tocor(str(square))
                    what, rook = piece.to(square)
                    if nColor in king.square.checked:
                        piece.tp(psquare)
                        raise Exception
                    canvas.moveto(opieces.get(piece), x, y)
                    if what == "Castling":
                        x, y = tocor(str(rook.square))
                        canvas.moveto(opieces.get(rook), x, y)
                    elif what == "Promotion":
                        canvas.delete(clickID)
                        global popup
                        popup = Canvas(root, width=400, height=100, bg='#FDFDFD')
                        popup.place(x = 345, y = 345, anchor="center")
                        position = piece.square
                        if color == "White":
                            queen = wqueen
                            rook = wrook
                            bishop = wbishop
                            knight = wknight
                        else:
                            queen = bqueen
                            rook = brook
                            bishop = bbishop
                            knight = bknight

                        bt1 = Button(height=100, width=100, image=queen, command=lambda c=color,w="Queen": promotion(c,w, position, queen),bg='#FDFDFD')
                        bt2 = Button(height=100, width=100, image=rook, command=lambda c=color,w="Rook": promotion(c,w,position, rook ),bg='#FDFDFD')
                        bt3 = Button(height=100, width=100, image=bishop, command=lambda c=color,w="Bishop": promotion(c,w,position, bishop),bg='#FDFDFD')
                        bt4 = Button(height=100, width=100, image=knight, command=lambda c=color,w="Knight": promotion(c,w,position, knight),bg='#FDFDFD')
                        bt1.place(x=195, y=345, anchor='center')
                        bt2.place(x=295, y=345, anchor='center')
                        bt3.place(x=395, y=345, anchor='center')
                        bt4.place(x=495, y=345, anchor='center')
                        bt1.lift()
                        bt2.lift()
                        bt3.lift()
                        bt4.lift()
                        var.set(1)
                        popup.wait_variable(var)
                        popup.destroy()
                        bt1.destroy()
                        bt2.destroy()
                        bt3.destroy()
                        bt4.destroy()
                        pieces[pieces.index(piece)] = "Null"
                        del piece
                        var.set(0)
                    for i, x in enumerate(pieces):
                        if x == "Null":
                            canvas.delete(lpieces[i])

                lmove = color
                if not check(nColor):
                    print("Szach Mat")
            except:
                pass
            square.clicked = False
            lclick.clicked = False
            canvas.delete(clickID)
    else:
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
                king = pieces[15] if piece.color == "White" else pieces[31]
                nColor = "Black" if king.color == "White" else "White"
                psquare = piece.square
                x, y = tocor(str(square))
                what, rook = piece.to(square)
                if nColor in king.square.checked:
                    piece.tp(psquare)
                    raise Exception
                canvas.moveto(opieces.get(piece), x, y)
                if what == "Castling":
                    x, y = tocor(str(rook.square))
                    canvas.moveto(opieces.get(rook), x, y)
                square.clicked = False
                lclick.clicked = False
                return True
            except:
                square.clicked = False
                lclick.clicked = False
                return False



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
def promotion(color, piece_type, position, image):
    piece = Piece(color, piece_type, position)
    if color == "White":
        whites.append(piece)
        pieces.append(whites[-1])
    else:
        blacks.append(piece)
        pieces.append(blacks[-1])
    lpieces.append(canvas.create_image(tocor(str(position)),image=image,anchor = 'nw'))
    opieces[pieces[-1]] = lpieces[-1]
    var.set(2)
def check(color):
    is_move = False
    colors = whites if color == "White" else blacks
    for x in colors:
        for y in set(move(x, True)) | set(capture(x)):
            tmove(x.square, False)
            is_move = tmove(y, False) if not is_move else is_move
            print(is_move)
    return is_move
def getpiece(eventorigin):
    xc = eventorigin.x
    yc = eventorigin.y
    xc //= 5
    print(xc)
    popup.destroy()
def getsquare(eventorigin):
    if var.get() == 0:
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
            checking()
            tmove(square)
root = Tk()
root.title("Szachy")
root.geometry("691x691")
root.resizable(False, False)

lmove = "Black"

var = IntVar(value=0)
clicking = ["Null"]
checked = list()

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
clicked = PhotoImage(file="img/clicked.png")
lost = PhotoImage(file="img/lost.png")
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

