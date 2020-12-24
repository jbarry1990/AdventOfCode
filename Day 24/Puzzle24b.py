"""
Puzzle #24a - AdventOfCode
1. Read inputs from file. each line represents a series of moves from the center hexagonal tile at the center of the floor.
2. Iterate through the list of tiles to be changed and flip the color of each tile. All tiles start as white
3. Using the following rules iterate through 100 iterations and simultaneously determine which tiles get switched to white and which get switched to black using the following rules
    1. If a tile is black and has 0 or more than 2 black tiles as neighbors then flip to white
    2. If a tile is white and has 2 black tiles as neighbors then flip to black
    Otherwise tiles don't change
4. Determine how many black tiles are flipped up at the end of the 100 iterations and output the result
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

def LivingFloor(Colors):
    AddedColors = Colors.copy()
    

    for Tile in Colors:
        TileCoordinates = Tile.split(",")
        for Index, Coordinate in enumerate(TileCoordinates):
            TileCoordinates[Index] = int(Coordinate)
        Neighbors = []
        Neighbors.append([TileCoordinates[0]+1, TileCoordinates[1], TileCoordinates[2]-1])
        Neighbors.append([TileCoordinates[0], TileCoordinates[1]+1, TileCoordinates[2]-1])
        Neighbors.append([TileCoordinates[0]+1, TileCoordinates[1]-1, TileCoordinates[2]])
        Neighbors.append([TileCoordinates[0]-1, TileCoordinates[1]+1, TileCoordinates[2]])
        Neighbors.append([TileCoordinates[0], TileCoordinates[1]-1, TileCoordinates[2]+1])
        Neighbors.append([TileCoordinates[0]-1, TileCoordinates[1], TileCoordinates[2]+1])

        for Coordinate in Neighbors:
            Coordinate = [str(Number) for Number in Coordinate]
            Key = ",".join(Coordinate)
            if Key not in AddedColors:
                AddedColors[Key] = 0

    UpdatedTiles = AddedColors.copy()   
    for Tile in AddedColors:
        
        IsBlack = False
        if AddedColors[Tile] % 2 != 0:
            IsBlack = True

        BlackCount = 0
        
        TileCoordinates = Tile.split(",")
        for Index, Coordinate in enumerate(TileCoordinates):
            TileCoordinates[Index] = int(Coordinate)
        Neighbors = []
        Neighbors.append([TileCoordinates[0]+1, TileCoordinates[1], TileCoordinates[2]-1])
        Neighbors.append([TileCoordinates[0], TileCoordinates[1]+1, TileCoordinates[2]-1])
        Neighbors.append([TileCoordinates[0]+1, TileCoordinates[1]-1, TileCoordinates[2]])
        Neighbors.append([TileCoordinates[0]-1, TileCoordinates[1]+1, TileCoordinates[2]])
        Neighbors.append([TileCoordinates[0], TileCoordinates[1]-1, TileCoordinates[2]+1])
        Neighbors.append([TileCoordinates[0]-1, TileCoordinates[1], TileCoordinates[2]+1])

        for Coordinate in Neighbors:
            Coordinate = [str(Number) for Number in Coordinate]
            Key = ",".join(Coordinate)
            if Key in AddedColors:
                if AddedColors[Key] % 2 != 0:
                    BlackCount += 1
        if IsBlack == True:
            if BlackCount == 0 or BlackCount > 2:
                UpdatedTiles[Tile] += 1
        else:
            if BlackCount == 2:
                UpdatedTiles[Tile] += 1
        
    return UpdatedTiles

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
    for Day in range(100):
        Colors = LivingFloor(Colors)

    Answer = CountBlack(Colors)

    print("Part 2: ", Answer)    
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
