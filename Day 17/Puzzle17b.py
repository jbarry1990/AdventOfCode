"""
Puzzle #17a - AdventOfCode
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInputs.txt", "r")
    Grid = []

    for Entry in File:
        inner = []
        for Character in Entry:
            inner.append(Character.strip())
        Grid.append(inner)

    return Grid

def DetermineActive(grid):
    ActiveStates = []
    for i, Row in enumerate(grid):
        for j, Column in enumerate(Row):
            if Column == "#":
                ActiveStates.append((i,j,0,0))
           
    return ActiveStates

def Cycle(ActiveState):
    Active = set(ActiveState)
    UpdatedState = []

    NeighborsOfActives = set()

    for x, y, z, w in ActiveState:
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        NeighborsOfActives.add((x+dx, y+dy, z+dz, w+dw))

    for NeighborX, NeighborY, NeighborZ, NeighborW in NeighborsOfActives:
        Count = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        if (NeighborX + dx, NeighborY + dy, NeighborZ + dz, NeighborW + dw) in Active:
                            Count +=1
        Count -= (NeighborX, NeighborY, NeighborZ, NeighborW) in Active
        if Count ==3 or (Count ==2 and (NeighborX, NeighborY, NeighborZ, NeighborW) in Active):
            UpdatedState.append((NeighborX, NeighborY, NeighborZ, NeighborW))

    return UpdatedState
def main():
    t_start = time()
    
    Grid = ReadInFile()
    ActiveState = DetermineActive(Grid)

    for NumCycles in range(6):
        ActiveState = Cycle(ActiveState)

    Answer = len(ActiveState)
    
    print("Part 1: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
