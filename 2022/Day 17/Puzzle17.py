def ReadInputs():
        File = open("./Inputs.txt", "r")
        Line = File.read().strip()
        Directions = [Char for Char in Line]
        
        return Directions

def get_piece(t, y):
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def move_left(piece):
    if any([x==0 for (x,y) in piece]):
        return piece
    return set([(x-1,y) for (x,y) in piece])

def move_right(piece):
    if any([x==6 for (x,y) in piece]):
        return piece
    return set([(x+1,y) for (x,y) in piece])

def move_down(piece):
    return set([(x,y-1) for (x,y) in piece])
def move_up(piece):
    return set([(x,y+1) for (x,y) in piece])

def signature(R):
    maxY = max([y for (x,y) in R])
    return frozenset([(x,maxY-y) for (x,y) in R if maxY-y<=30])

def solveA(Directions):
    R = set([(x,0) for x in range(7)])
    top = 0
    i = 0
    t = 0

    while t < 2022:
        piece = get_piece(t%5, top+4)
        while True:
            # pushed -> down
            if Directions[i]=='<':
                piece = move_left(piece)
                if piece & R:
                    piece = move_right(piece)
            else:
                piece = move_right(piece)
                if piece & R:
                    piece = move_left(piece)
            i = (i+1)%len(Directions)
            piece = move_down(piece)
            if piece & R:
                piece = move_up(piece)
                R |= piece
                top = max([y for (x,y) in R])
                break
        t +=1
    return top

def solveB(Directions):
    L = 1000000000000

    SEEN = {}
    added = 0
    R = set([(x,0) for x in range(7)])
    top = 0
    i = 0
    t = 0

    while t < L:
        piece = get_piece(t%5, top+4)
        while True:
            # pushed -> down
            if Directions[i]=='<':
                piece = move_left(piece)
                if piece & R:
                    piece = move_right(piece)
            else:
                piece = move_right(piece)
                if piece & R:
                    piece = move_left(piece)
            i = (i+1)%len(Directions)
            piece = move_down(piece)
            if piece & R:
                piece = move_up(piece)
                R |= piece
                top = max([y for (x,y) in R])

                SR = (i, t%5, signature(R))
                if SR in SEEN and t>=2022:
                    (oldt, oldy) = SEEN[SR]
                    dy = top-oldy
                    dt = t-oldt
                    amt = (L-t)//dt
                    added += amt*dy
                    t += amt*dt
                    assert t<=L
                SEEN[SR] = (t,top)
                break
        t +=1
    return top+added

def main():

    Directions=ReadInputs()
    Part1=solveA(Directions)
    print("Answer: ", Part1)
    Part2=solveB(Directions)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
