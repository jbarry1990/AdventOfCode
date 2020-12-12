"""
Puzzle #11a - AdventOfCode
Read in seat map
Determine which seats will be occupied and which seats will be vacant following these rules
1. If a seat is vacant and all adjacent seats are vacant then the seat becomes occupied
2. If a set is occupied and has at least 4 adjacent seats occupied it becomes vacant
3. Floor never changes
Iterate through status until seats don't change
Output the total number of occupied seats

"""
import math
from copy import copy, deepcopy

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")

    SeatMap = [[Character for Character in Line.strip()] for Line in File]
            
    return SeatMap

def UpdateSeats(SeatMap):
    NextSeatMap = deepcopy(SeatMap)
    NumberOfRows = len(NextSeatMap)
    NumberOfColumns = len(NextSeatMap[0])
    SeatsChanged = 0

    for i, Row in enumerate(NextSeatMap):
        for j, Column in enumerate(Row):
            OccupiedCount = 0
            
            if NextSeatMap[i][j] == ".":
                continue
            
            #Is a corner
            if (i == 0 and j == 0) or (i == 0 and j == NumberOfColumns-1) or (i == NumberOfRows-1 and j == 0) or (i == NumberOfRows-1 and j==NumberOfColumns-1):
                if SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                    
            #Is top row       
            elif i == 0 and (j != 0 or j != NumberOfColumns-1):
                Adjacent = [SeatMap[i][j-1], SeatMap[i][j+1], SeatMap[i+1][j], SeatMap[i+1][j-1], SeatMap[i+1][j+1]]
                for Seat in Adjacent:
                    if Seat == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 4 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1
                    
            #Is bottom row    
            elif i == NumberOfRows-1 and (j != 0 or j != NumberOfColumns-1):
                Adjacent = [SeatMap[i][j-1], SeatMap[i][j+1], SeatMap[i-1][j], SeatMap[i-1][j-1], SeatMap[i-1][j+1]]
                for Seat in Adjacent:
                    if Seat == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 4 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Is Left Column               
            elif (i != 0 or i !=NumberOfRows-1) and j == 0:
                Adjacent = [SeatMap[i][j+1], SeatMap[i-1][j], SeatMap[i+1][j], SeatMap[i-1][j+1], SeatMap[i+1][j+1]]
                for Seat in Adjacent:
                    if Seat == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 4 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Is Right Column
            elif (i != 0 or i != NumberOfRows-1) and j == NumberOfColumns-1:
                Adjacent = [SeatMap[i][j-1], SeatMap[i-1][j], SeatMap[i+1][j], SeatMap[i-1][j-1], SeatMap[i+1][j-1]]
                for Seat in Adjacent:
                    if Seat == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 4 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Every Other Seat
            else:
                Adjacent = [SeatMap[i][j-1], SeatMap[i][j+1], SeatMap[i-1][j], SeatMap[i+1][j], SeatMap[i-1][j-1], SeatMap[i+1][j-1], SeatMap[i-1][j+1], SeatMap[i+1][j+1]]
                for Seat in Adjacent:
                    if Seat == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 4 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

    return SeatsChanged, NextSeatMap

def NumberOfSeats(SeatMap):
    SeatsChanged, NewSeatMap = UpdateSeats(SeatMap)  
    while SeatsChanged != 0:
        SeatsChanged,NewSeatMap = UpdateSeats(NewSeatMap)

    OccupiedSeats = 0
    for Row in NewSeatMap:
        for Column in Row:
            if Column == "#":
                OccupiedSeats += 1
    return OccupiedSeats

def main():
    SeatMap = ReadInFile()
    OccupiedSeats = NumberOfSeats(SeatMap)
    print("Part 1: ", OccupiedSeats)


if __name__ == "__main__":
    main()
