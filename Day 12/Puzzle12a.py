"""
Puzzle #12a - AdventOfCode
Read in navigation instructions
Route based on instructions
Output destination
"""

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Navigation = []

    for Entry in File:
        Navigation.append((Entry[0], int(Entry[1:].strip())))
            
    return Navigation

def Navigate(Navigation):
    """
    North/South = Heading[0]
    East/West = Heading[1]
    """
    Direction = ["North", "East", "South", "West"]
    Heading = [0, 0]
    CurrentHeading = "East"

    for Instruction in Navigation:
        if Instruction[0] == "N":
            Heading[0] += Instruction[1]
            
        elif Instruction[0] == "S":
            Heading[0] -= Instruction[1]
            
        elif Instruction[0] == "E":
            Heading[1] += Instruction[1]
            
        elif Instruction[0] == "W":
            Heading[1] -= Instruction[1]
            
        elif Instruction[0] == "L":
            NumberOfIndicesToMove = int(Instruction[1]/90)
            CurrentIndex = Direction.index(CurrentHeading)
            if(CurrentIndex-NumberOfIndicesToMove <0):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentHeading = Direction[CurrentIndex+Recipricol]
            else:
                CurrentHeading = Direction[CurrentIndex-NumberOfIndicesToMove]
                
        elif Instruction[0] == "R":
            NumberOfIndicesToMove = int(Instruction[1]/90)
            CurrentIndex = Direction.index(CurrentHeading)
            if(CurrentIndex+NumberOfIndicesToMove >3):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentHeading = Direction[CurrentIndex-Recipricol]
            else:

                CurrentHeading = Direction[CurrentIndex+NumberOfIndicesToMove]
                
        elif Instruction[0] == "F":
            if CurrentHeading == "North":
                Heading[0] += Instruction[1]
            if CurrentHeading == "South":
                Heading[0] -= Instruction[1]
            if CurrentHeading == "East":
                Heading[1] += Instruction[1]
            if CurrentHeading == "West":
                Heading[1] -= Instruction[1]
                
    return Heading[0], Heading[1]

def main():
    Navigation = ReadInFile()
    NorthSouth, EastWest = Navigate(Navigation)
    print("North/South: ", NorthSouth)
    print("East/West: ", EastWest)
    Distance = abs(NorthSouth)+abs(EastWest)

    print("Part 1: ", Distance)


if __name__ == "__main__":
    main()
