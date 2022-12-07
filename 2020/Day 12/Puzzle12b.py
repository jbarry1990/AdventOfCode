"""
Puzzle #12b - AdventOfCode
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
    Heading = [0,0]
    Direction = ["North", "East", "South", "West"]
    HeadingOffset = [1, 10]
    CurrentMajor = "East"
    CurrentMinor = "North"
    Counter = -1

    for Instruction in Navigation:
        
        if Instruction[0] == "N":
            if CurrentMajor == "North":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "South"
                    continue
                    
            if CurrentMajor == "South":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "North"
                    continue
                    
            if CurrentMinor == "North":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "South"
                    continue
                    
            if CurrentMinor == "South":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0] -=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "North"
                    continue
                

        elif Instruction[0] == "S":
            if CurrentMajor == "North":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "South"
                    continue
                    
            if CurrentMajor == "South":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "North"
                    continue
                    
            if CurrentMinor == "North":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "South"
                    continue
                    
            if CurrentMinor == "South":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0] +=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "North"
                    continue
                    
        elif Instruction[0] == "E":
            if CurrentMajor == "East":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "West"
                    continue
                    
            if CurrentMajor == "West":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "East"
                    continue
                    
            if CurrentMinor == "East":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "West"
                    continue
                    
            if CurrentMinor == "West":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0] -=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "East"
                    continue
            
        elif Instruction[0] == "W":
            if CurrentMajor == "East":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "West"
                    continue
                    
            if CurrentMajor == "West":
                PreviousHeadingOffset = HeadingOffset[1]
                HeadingOffset[1]+=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[1] < 0:
                    HeadingOffset[1] *=-1
                    CurrentMajor = "East"
                    continue
                    
            if CurrentMinor == "East":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0]-=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "West"
                    continue
                    
            if CurrentMinor == "West":
                PreviousHeadingOffset = HeadingOffset[0]
                HeadingOffset[0] +=Instruction[1]
                if PreviousHeadingOffset >= 0 and HeadingOffset[0] < 0:
                    HeadingOffset[0] *=-1
                    CurrentMinor = "East"
                    continue
            
        elif Instruction[0] == "L":
            NumberOfIndicesToMove = int(Instruction[1]/90)
            CurrentMajorIndex = Direction.index(CurrentMajor)
            CurrentMinorIndex = Direction.index(CurrentMinor)
            
            if(CurrentMajorIndex-NumberOfIndicesToMove <0):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentMajor = Direction[CurrentMajorIndex+Recipricol]
            else:
                CurrentMajor = Direction[CurrentMajorIndex-NumberOfIndicesToMove]
            
            if(CurrentMinorIndex-NumberOfIndicesToMove <0):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentMinor = Direction[CurrentMinorIndex+Recipricol]
            else:
                CurrentMinor = Direction[CurrentMinorIndex-NumberOfIndicesToMove]
            
        elif Instruction[0] == "R":
            NumberOfIndicesToMove = int(Instruction[1]/90)
            CurrentMajorIndex = Direction.index(CurrentMajor)
            CurrentMinorIndex = Direction.index(CurrentMinor)
            
            if(CurrentMajorIndex+NumberOfIndicesToMove >3):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentMajor = Direction[CurrentMajorIndex-Recipricol]
            else:
                CurrentMajor = Direction[CurrentMajorIndex+NumberOfIndicesToMove]
                
            if(CurrentMinorIndex+NumberOfIndicesToMove >3):
                Recipricol = 4 - NumberOfIndicesToMove
                CurrentMinor = Direction[CurrentMinorIndex-Recipricol]
            else:
                CurrentMinor = Direction[CurrentMinorIndex+NumberOfIndicesToMove]
                
        elif Instruction[0] == "F":
            if CurrentMajor == "North":
                Heading[0] += (HeadingOffset[1] * Instruction[1])
            elif CurrentMinor == "North":
                Heading[0] += (HeadingOffset[0] * Instruction[1])
                
            if CurrentMajor == "South":
                Heading[0] -= (HeadingOffset[1] * Instruction[1])
            elif CurrentMinor == "South":
                Heading[0] -= HeadingOffset[0] * Instruction[1]
                
            if CurrentMajor == "East":
                Heading[1] += (HeadingOffset[1] * Instruction[1])
            elif CurrentMinor == "East":
                Heading[1] += (HeadingOffset[0] * Instruction[1])
                
            if CurrentMajor == "West":
                Heading[1] -= (HeadingOffset[1] * Instruction[1])
            elif CurrentMinor == "West":
                Heading[1] -= (HeadingOffset[0] * Instruction[1])

    return Heading[0], Heading[1]

def main():
    Navigation = ReadInFile()
    NorthSouth, EastWest = Navigate(Navigation)
    Distance = abs(NorthSouth)+abs(EastWest)

    print("Part 2: ", Distance)


if __name__ == "__main__":
    main()
