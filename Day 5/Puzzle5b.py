"""
Puzzle #5b - AdventOfCode
Read in a list of boarding passes
Determine the seat id for each boarding pass
Create list of all seats between minimum seat id and maximum seat id
Compare that list to the seat id list to determine which seat is missing.
Print missing seat aka my seat
"""

import math

def ReadInFile():
    File = open("./BoardingPasses.txt", "r")
    BoardingPasses = []

    for Entry in File:
            BoardingPasses.append(Entry.rstrip())

    return BoardingPasses

def DetermineRowColumn(BoardingPasses):
    RowColumnList = []
    for BoardingPass in BoardingPasses:
        PossibleRows = []
        for Index in range(128):
            PossibleRows.append(Index)
            
        PossibleColumns = []
        for Index in range(8):
            PossibleColumns.append(Index)
            
        for Character in BoardingPass[:-3]:
            Size = len(PossibleRows)
            HalfSize = Size/2
            if Character == "F":
                PossibleRows = PossibleRows[0:int(HalfSize)]

            else:
                PossibleRows = PossibleRows[int(HalfSize):]

                 
        for Character in BoardingPass[-3:]:
            Size = len(PossibleColumns)
            HalfSize = Size/2
            if Character == "L":
                PossibleColumns = PossibleColumns[0:int(HalfSize)]

            else:
                PossibleColumns = PossibleColumns[int(HalfSize):]

        RowColumnList.append((PossibleRows[0], PossibleColumns[0]))

    return RowColumnList

def MapSeatID(SeatAssignments):
    SeatIDList = []
    for SeatAssignment in SeatAssignments:
        SeatID = SeatAssignment[0] * 8 + SeatAssignment[1]
        SeatIDList.append(SeatID)

    return SeatIDList

def DetermineMinMaxSeatID(SeatIDList):
    HighestSeatID = 0
    LowestSeatID = 1023
    for SeatID in SeatIDList:
        if SeatID > HighestSeatID:
            HighestSeatID = SeatID
            
        elif SeatID < LowestSeatID:
            LowestSeatID = SeatID
            
        
    return LowestSeatID, HighestSeatID

def DetermineMySeat(MinimumSeatID, MaximumSeatID, SeatIDList):
    AllSeats = []
    MySeat = 0
    for Index in range(MinimumSeatID, MaximumSeatID+1):
        AllSeats.append(Index)

    SeatIDList.sort()

    ComparisonList = zip(AllSeats, SeatIDList)

    for x,y in ComparisonList:
        if x != y:
            MySeat = x
            break

    return MySeat

def main():
    
    BoardingPasses = ReadInFile()
    SeatAssignments = DetermineRowColumn(BoardingPasses)
    ListOfSeatIDs = MapSeatID(SeatAssignments)
    MinimumSeatID, MaximumSeatID = DetermineMinMaxSeatID(ListOfSeatIDs)
    MySeat = DetermineMySeat(MinimumSeatID, MaximumSeatID, ListOfSeatIDs)

    print("My seat is: ", MySeat)

if __name__ == "__main__":
    main()
