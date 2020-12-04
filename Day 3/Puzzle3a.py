"""
Puzzle #3a - AdventOfCode
Read in a map
Duplicate the map to the right to cover the necessary size
Scan the map along the given line for trees
Keep track of how many trees are encountered
"""
import math

def ReadInFile():
    File = open("./MapFragment.txt", "r")
    MapFragment = []
    
    for Entries in File:
        MapFragment.append(Entries.rstrip())

    print("NumberOfEntries:",len(MapFragment))
    return MapFragment

def GenerateFullMap(MapFragment, SlopeX):
    MapLength = len(MapFragment)
    MapWidth = len(MapFragment[0])


    IterationsPerMapFragment = MapWidth/SlopeX
    IterationsPerMapFragment = int(IterationsPerMapFragment)
    NumberMapFragmentsNeeded = math.ceil(MapLength/IterationsPerMapFragment)

    FullMap = []
    Temp = ""
    for Slice in MapFragment:
        for x in range(0, NumberMapFragmentsNeeded):
            Temp = Temp + Slice
        FullMap.append(Temp)
        Temp = ""

    return FullMap

def NavigateMap(FullMap, SlopeX, SlopeY):
    NextXLocation = 0
    TreesHit = 0

    for YIndex, Slice in enumerate(FullMap):
        if YIndex%SlopeY == 0:
            if YIndex == 0:
                if Slice[0] == "#":
                    print("Tree found on line ", YIndex+1)
                    TreesHit +=1
            else:
                if Slice[NextXLocation] == "#":
                    print("Tree found on line ", YIndex+1)
                    TreesHit +=1
                           
            NextXLocation = NextXLocation + SlopeX
            
        
    return TreesHit

def main():

    SlopeX = 3
    SlopeY = 1
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX)
    NumberTreesHit = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Ouch! I hit ", NumberTreesHit, "trees")
        
if __name__ == "__main__":
    main()
