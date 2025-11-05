from GUI import root
csquare = None
psquare = None
def tmove(square):
    global csquare, psquare
    psquare = csquare
    csquare = square
    if psquare != csquare and psquare.occupant != "Null":
        psquare.occupant.move(csquare)
        csquare = None
        psquare = None
root.mainloop()

