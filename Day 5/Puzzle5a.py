"""
Puzzle #5a - AdventOfCode
Read in a list of boarding passes
Determine the seat id for each boarding pass
print the highest seat id
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

def DetermineHighestSeatID(SeatIDList):
    HighestSeatID = 0
    for SeatID in SeatIDList:
        if SeatID > HighestSeatID:
            HighestSeatID = SeatID
        
    return HighestSeatID
                
        

def main():
    
    BoardingPasses = ReadInFile()
    SeatAssignments = DetermineRowColumn(BoardingPasses)
    ListOfSeatIDs = MapSeatID(SeatAssignments)
    Answer = DetermineHighestSeatID(ListOfSeatIDs)

    print("The highest Seat ID is: ", Answer)

if __name__ == "__main__":
    main()
