"""
Puzzle #3b - AdventOfCode
Read in a map
Duplicate the map to the right to cover the necessary size
Scan the map along the given line for trees
Keep track of how many trees are encountered for each case and multiply the results together
"""
import math

def ReadInFile():
    File = open("./MapFragment.txt", "r")
    MapFragment = []
    
    for Entries in File:
        MapFragment.append(Entries.rstrip())

    print("NumberOfEntries:",len(MapFragment))
    return MapFragment

def GenerateFullMap(MapFragment, SlopeX, SlopeY):
    MapLength = len(MapFragment)
    MapWidth = len(MapFragment[0])
    
    NumberLinesToIterate = MapLength/SlopeY
    NumberLinesToIterate = int(NumberLinesToIterate)
    IterationsPerMapFragment = MapWidth/SlopeX
    IterationsPerMapFragment = int(IterationsPerMapFragment)
    NumberMapFragmentsNeeded = math.ceil(NumberLinesToIterate/IterationsPerMapFragment)

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
                    TreesHit +=1
                           
            NextXLocation = NextXLocation + SlopeX
            
        
    return TreesHit

def main():

    SlopeX = 1
    SlopeY = 1
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX, SlopeY)
    NumberTreesHitCase1 = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Case 1:  ", NumberTreesHitCase1, "trees hit")

    SlopeX = 3
    SlopeY = 1
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX, SlopeY)
    NumberTreesHitCase2 = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Case 2:  ", NumberTreesHitCase2, "trees hit")

    SlopeX = 5
    SlopeY = 1
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX, SlopeY)
    NumberTreesHitCase3 = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Case 3:  ", NumberTreesHitCase3, "trees hit")

    SlopeX = 7
    SlopeY = 1
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX, SlopeY)
    NumberTreesHitCase4 = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Case 4:  ", NumberTreesHitCase4, "trees hit")

    SlopeX = 1
    SlopeY = 2
    
    MapFragment = ReadInFile()
    FullMap = GenerateFullMap(MapFragment, SlopeX, SlopeY)
    NumberTreesHitCase5 = NavigateMap(FullMap, SlopeX, SlopeY)
    print("Case 5:  ", NumberTreesHitCase5, "trees hit")

    TreeMultiplication = NumberTreesHitCase1 * NumberTreesHitCase2 * NumberTreesHitCase3 * NumberTreesHitCase4* NumberTreesHitCase5
    print("Tree Multiplication:  ", TreeMultiplication)
        
if __name__ == "__main__":
    main()
