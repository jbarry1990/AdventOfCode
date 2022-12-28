def ReadInputs():
        File = open("./Inputs.txt", "r")
        Positions = {}
        Count = 0
        Grid = [list(Line.strip()) for Line in File]
        for row_i, row in enumerate(Grid):
            for col_i, col in enumerate(row):
                if col == "#":
                    Positions[Count] = [row_i, col_i]
                    Count +=1
        return Positions
    
def solveA(Positions, Rounds):
    Directions = [[-1,0], [1,0], [0,-1], [0,1]]
    for _ in range(Rounds):
        ProposedLocation = {}

        for Elf, Location in Positions.items():
            x = Location[0]
            y = Location[1]
            HasNeighbors = False
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    if any(True for Key,Value in Positions.items() if [x+dx, y+dy] == Value):
                        HasNeighbors = True
            if HasNeighbors == False:
                continue

            for Direction in Directions:
                if Direction == [-1,0]:
                    LeftNeighbor = [x-1,y-1]
                    MiddleNeighbor = [x-1,y]
                    RightNeighbor = [x-1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [1,0]:
                    LeftNeighbor = [x+1,y-1]
                    MiddleNeighbor = [x+1,y]
                    RightNeighbor = [x+1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [0,1]:
                    LeftNeighbor = [x-1,y+1]
                    MiddleNeighbor = [x,y+1]
                    RightNeighbor = [x+1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [0,-1]:
                    LeftNeighbor = [x-1,y-1]
                    MiddleNeighbor = [x,y-1]
                    RightNeighbor = [x+1,y-1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
        # Check proposed locations to see if only one elf wants to move then move
        for Key,Value in ProposedLocation.items():
            if len(Value) ==1:
                Positions[Value[0]] = list(Key)
        # Rotate the direction
        move = Directions.pop(0)
        Directions.append(move)

    minx = min(Position[0] for Key,Position in Positions.items())
    maxx = max(Position[0] for Key,Position in Positions.items())+1
    miny = min(Position[1] for Key,Position in Positions.items())
    maxy = max(Position[1] for Key,Position in Positions.items())+1
    area = (abs(maxx-minx))*(abs(maxy-miny))

    return area-len(Positions)

def print_grid(Positions):
    minx = min(Position[0] for Key,Position in Positions.items())
    maxx = max(Position[0] for Key,Position in Positions.items())+1
    miny = min(Position[1] for Key,Position in Positions.items())
    maxy = max(Position[1] for Key,Position in Positions.items())+1

    grid = []
    rows = []
    for row in range(minx,maxx):
        for col in range(miny, maxy):
            if any(True for Key,Value in Positions.items() if [row, col] == Value):
                rows.append("#")
            else:
                rows.append(".")
        grid.append(rows)
        rows = []

    for rows in grid:
        print("".join(rows))

    return 

def solveB(Positions):
    Directions = [[-1,0], [1,0], [0,-1], [0,1]]
    Processing = True
    Count = 0
    while Processing == True:
        Count += 1
        ProposedLocation = {}
        SomeoneMoved = False
        for Elf, Location in Positions.items():
            x = Location[0]
            y = Location[1]
            HasNeighbors = False
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    if any(True for Key,Value in Positions.items() if [x+dx, y+dy] == Value):
                        HasNeighbors = True
            if HasNeighbors == False:
                continue
            SomeoneMoved = True
            for Direction in Directions:
                if Direction == [-1,0]:
                    LeftNeighbor = [x-1,y-1]
                    MiddleNeighbor = [x-1,y]
                    RightNeighbor = [x-1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [1,0]:
                    LeftNeighbor = [x+1,y-1]
                    MiddleNeighbor = [x+1,y]
                    RightNeighbor = [x+1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [0,1]:
                    LeftNeighbor = [x-1,y+1]
                    MiddleNeighbor = [x,y+1]
                    RightNeighbor = [x+1,y+1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                elif Direction == [0,-1]:
                    LeftNeighbor = [x-1,y-1]
                    MiddleNeighbor = [x,y-1]
                    RightNeighbor = [x+1,y-1]
                    if any(True for Key,Value in Positions.items() if LeftNeighbor == Value or MiddleNeighbor == Value or RightNeighbor == Value):
                        continue
                    if tuple(MiddleNeighbor) in ProposedLocation:
                        ProposedLocation[tuple(MiddleNeighbor)].append(Elf)
                    else:
                        ProposedLocation[tuple(MiddleNeighbor)] = [Elf]
                    break
                # Check proposed locations to see if only one elf wants to move then move
        for Key,Value in ProposedLocation.items():
            if len(Value) ==1:
                Positions[Value[0]] = list(Key)
            # Rotate the direction
        move = Directions.pop(0)
        Directions.append(move)

        #print_grid(Positions)
        #print("----------------------------------------")

        if SomeoneMoved == False:
            Processing = False
            break
        


    return Count

def main():

    Input=ReadInputs()
    Part1=solveA(Input, 10)
    print("Answer: ", Part1)
    Input=ReadInputs()
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
