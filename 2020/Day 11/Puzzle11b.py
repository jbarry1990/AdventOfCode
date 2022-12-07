"""
Puzzle #11b - AdventOfCode
Read in seat map
Determine which seats will be occupied and which seats will be vacant following these rules
1. If a seat is vacant and all visible seats are vacant then the seat becomes occupied
2. If a set is occupied and has at least 5 adjacent seats occupied it becomes vacant
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
            """
            DiagonalCounts[0]: UpLeft
            DiagonalCounts[1]: UpRight
            DiagonalCounts[2]: DownLeft
            DiagonalCounts[3]: DownRight
            """
            DiagonalCounts = [1 , 1 , 1, 1]
            
            if NextSeatMap[i][j] == ".":
                continue
            
            #Is a corner
            if (i == 0 and j == 0) or (i == 0 and j == NumberOfColumns-1) or (i == NumberOfRows-1 and j == 0) or (i == NumberOfRows-1 and j==NumberOfColumns-1):
                if SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                    
            #Is top row       
            elif i == 0 and (j > 0 or j <= NumberOfColumns-1):
                Adjacent = {}

                for di in range(i,NumberOfRows):
                    for dj in range(j, NumberOfColumns):

                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Down" not in Adjacent.keys():
                                Adjacent["Down"] = SeatMap[di][dj]
                                
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Right" not in Adjacent.keys():
                                Adjacent["Right"] = SeatMap[di][dj]
                                
                        if di == i + DiagonalCounts[3] and dj == j + DiagonalCounts[3]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[3] += 1
                                continue
                            elif "DownRight" not in Adjacent.keys():
                                Adjacent["DownRight"] = SeatMap[di][dj]
                                DiagonalCounts[3] = 1
                                
                    for dj in range(j,-1,-1):

                        if (di == i and dj ==j):
                            continue
                        
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Left" not in Adjacent.keys():
                                Adjacent["Left"] = SeatMap[di][dj]
                                
                        if di == (i + DiagonalCounts[2]) and dj == (j - DiagonalCounts[2]):
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[2] +=1
                                continue
                            elif "DownLeft" not in Adjacent.keys():
                                Adjacent["DownLeft"] = SeatMap[di][dj]
                                DiagonalCounts[2] = 1
                                
                for Key in Adjacent:
                    if Adjacent[Key] == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 5 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1
                    
            #Is bottom row    
            elif i == NumberOfRows-1 and (j != 0 or j != NumberOfColumns-1):
                Adjacent = {}

                for di in range(i, -1,-1):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Up" not in Adjacent.keys():
                                Adjacent["Up"] = SeatMap[di][dj]
                                
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Right" not in Adjacent.keys():
                                Adjacent["Right"] = SeatMap[di][dj]
                                
                        if di == i - DiagonalCounts[1] and dj == j + DiagonalCounts[1]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[1] += 1
                                continue
                            elif "UpRight" not in Adjacent.keys():
                                Adjacent["UpRight"] = SeatMap[di][dj]
                                DiagonalCounts[1] = 1
                                
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue
                        
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Left" not in Adjacent.keys():
                                Adjacent["Left"] = SeatMap[di][dj]
                                
                        if di == i - DiagonalCounts[0] and dj == j - DiagonalCounts[0]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[0] += 1
                                continue
                            elif "UpLeft" not in Adjacent.keys():
                                Adjacent["UpLeft"] = SeatMap[di][dj]
                                DiagonalCounts[0] = 1

                for Key in Adjacent:
                    if Adjacent[Key] == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 5 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Is Left Column               
            elif (i != 0 or i !=NumberOfRows-1) and j == 0:
                Adjacent = {}

                for di in range(i, -1,-1):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Up" not in Adjacent.keys():
                                Adjacent["Up"] = SeatMap[di][dj]
                                
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Right" not in Adjacent.keys():
                                Adjacent["Right"] = SeatMap[di][dj]
                                
                        if di == i - DiagonalCounts[1] and dj == j + DiagonalCounts[1]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[1] += 1
                                continue
                            elif "UpRight" not in Adjacent.keys():
                                Adjacent["UpRight"] = SeatMap[di][dj]
                                DiagonalCounts[1] = 1
                                
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue

                for di in range(i,NumberOfRows):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Down" not in Adjacent.keys():
                                Adjacent["Down"] = SeatMap[di][dj]
                                
                        if di == i + DiagonalCounts[3] and dj == j + DiagonalCounts[3]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[3] += 1
                                continue
                            elif "DownRight" not in Adjacent.keys():
                                Adjacent["DownRight"] = SeatMap[di][dj]
                                DiagonalCounts[3] = 1

                for Key in Adjacent:
                    if Adjacent[Key] == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 5 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Is Right Column
            elif (i != 0 or i != NumberOfRows-1) and j == NumberOfColumns-1:
                Adjacent = {}

                for di in range(i, -1,-1):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Up" not in Adjacent.keys():
                                Adjacent["Up"] = SeatMap[di][dj]
                                
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue
                        
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Left" not in Adjacent.keys():
                                Adjacent["Left"] = SeatMap[di][dj]
                                
                        if di == i - DiagonalCounts[0] and dj == j - DiagonalCounts[0]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[0] += 1
                                continue
                            elif "UpLeft" not in Adjacent.keys():
                                Adjacent["UpLeft"] = SeatMap[di][dj]
                                DiagonalCounts[0] = 1

                for di in range(i,NumberOfRows):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Down" not in Adjacent.keys():
                                Adjacent["Down"] = SeatMap[di][dj]
                                
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue
                                
                        if di == i + DiagonalCounts[2] and dj == j - DiagonalCounts[2]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[2] +=1
                                continue
                            elif "DownLeft" not in Adjacent.keys():
                                Adjacent["DownLeft"] = SeatMap[di][dj]
                                DiagonalCounts[2] = 1

                for Key in Adjacent:
                    if Adjacent[Key] == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 5 and SeatMap[i][j] == "#":
                    NextSeatMap[i][j] = "L"
                    SeatsChanged += 1

            #Every Other Seat
            else:
                Adjacent = {}

                for di in range(i, -1,-1):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Up" not in Adjacent.keys():
                                Adjacent["Up"] = SeatMap[di][dj]
                                   
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Right" not in Adjacent.keys():
                                Adjacent["Right"] = SeatMap[di][dj]
                                     
                        if di == i - DiagonalCounts[1] and dj == j + DiagonalCounts[1]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[1] += 1
                                continue
                            elif "UpRight" not in Adjacent.keys():
                                Adjacent["UpRight"] = SeatMap[di][dj]
                                DiagonalCounts[1] = 1
                                       
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue
                        
                        if(di == i and dj != j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Left" not in Adjacent.keys():
                                AdjacentIndex["Left"] = di,dj
                                
                        if di == i - DiagonalCounts[0] and dj == j - DiagonalCounts[0]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[0] += 1
                                continue
                            elif "UpLeft" not in Adjacent.keys():
                                Adjacent["UpLeft"] = SeatMap[di][dj]
                                DiagonalCounts[0] = 1

                for di in range(i,NumberOfRows):
                    for dj in range(j, NumberOfColumns):
                        if (di == i and dj ==j):
                            continue
                        
                        if (di != i and dj == j):
                            if SeatMap[di][dj] == ".":
                                continue
                            elif "Down" not in Adjacent.keys():
                                Adjacent["Down"] = SeatMap[di][dj]
                                    
                        if di == i + DiagonalCounts[3] and dj == j + DiagonalCounts[3]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[3] += 1
                                continue
                            elif "DownRight" not in Adjacent.keys():
                                Adjacent["DownRight"] = SeatMap[di][dj]
                                DiagonalCounts[3] = 1
                                         
                    for dj in range(j,-1,-1):
                        if (di == i and dj ==j):
                            continue
                                
                        if di == i + DiagonalCounts[2] and dj == j - DiagonalCounts[2]:
                            if SeatMap[di][dj] == ".":
                                DiagonalCounts[2] +=1
                                continue
                            elif "DownLeft" not in Adjacent.keys():
                                Adjacent["DownLeft"] = SeatMap[di][dj]
                                DiagonalCounts[2] = 1

                for Key in Adjacent:
                    if Adjacent[Key] == "#":
                        OccupiedCount +=1
                if OccupiedCount == 0 and SeatMap[i][j] == "L":
                    NextSeatMap[i][j] = "#"
                    SeatsChanged += 1
                elif OccupiedCount >= 5 and SeatMap[i][j] == "#":
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

def PrintMap(SeatMap):
    for Line in SeatMap:
        String = ""
        for Character in Line:
            String += Character
        print(String)
    print()

def main():
    SeatMap = ReadInFile()
    OccupiedSeats = NumberOfSeats(SeatMap)
    print("Part 2: ", OccupiedSeats)


if __name__ == "__main__":
    main()
