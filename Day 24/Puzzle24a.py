"""
Puzzle #24a - AdventOfCode
1. Read inputs from file. each line represents a series of moves from the center hexagonal tile at the center of the floor.
2. Iterate through the list of tiles to be changed and flip the color of each tile. All tiles start as white
3. Determine how many tiles have been switched to black.
4. Output the result
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Tiles = []
    Lines = []

    for Line in File:
        Lines.append(Line.strip())

    for Tile in Lines:
        Direction = []
        IgnoreNext = False
        for Index, Character in enumerate(Tile):
            if IgnoreNext == True:
                IgnoreNext = False
                continue
            if Character == "s" or Character == "n":
                Direction.append(Tile[Index:Index+2])
                IgnoreNext = True
            else:
                Direction.append(Character)
                if IgnoreNext == True:
                    IgnoreNext = False
                    
        Tiles.append(Direction)

    return Tiles

def FlipTiles(Tiles):
    Colors = {}
    for Tile in Tiles:
        StartingTile = [0,0,0]
        for Direction in Tile:
            if Direction == "ne":
                StartingTile[0] += 1
                StartingTile[2] -= 1
                
            elif Direction == "nw":
                StartingTile[1] += 1
                StartingTile[2] -= 1
                
            elif Direction == "e":
                StartingTile[0] += 1
                StartingTile[1] -= 1
                
            elif Direction == "w":
                StartingTile[0] -= 1
                StartingTile[1] += 1
                
            elif Direction == "se":
                StartingTile[1] -= 1
                StartingTile[2] += 1
                
            elif Direction == "sw":
                StartingTile[0] -= 1
                StartingTile[2] += 1
        StartingTile = [str(Number) for Number in StartingTile]        
        Key = ",".join(StartingTile)
        if Key in Colors:
            Colors[Key] += 1
        else:
            Colors[Key] = 1  
    return Colors

def CountBlack(Colors):
    Answer = 0
    for Tile in Colors:
        if Colors[Tile] % 2 != 0:
            Answer += 1
    
    return Answer

def main():
    t_start = time()

    Tiles = ReadInFile()
    Colors = FlipTiles(Tiles)
    Answer = CountBlack(Colors)

    print("Part 1: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
