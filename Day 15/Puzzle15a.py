"""
Puzzle #15a - AdventOfCode
Read in starting numbers. If the last number has been said before then the next number is the turn you are on - the turn the number was said on before. If it hasn't been said before
The next number is 0. Determine what the 2020th number spoken will be. 
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    StartingNumbers = []

    for Entry in File:
        for Number in Entry.split(","):
            StartingNumbers.append(int(Number))
        
    return StartingNumbers

def PlayGame(StartingNumbers):
    ContainsNumber = False
    NumberLocation = -1
    for CurrentNumberIndex in range(len(StartingNumbers),2020):
        PreviousNumber = StartingNumbers[CurrentNumberIndex - 1]

        for Index in reversed(range(len(StartingNumbers)-1)):
            if StartingNumbers[Index] == PreviousNumber:
                ContainsNumber = True
                NumberLocation = Index
                break;
                
        if ContainsNumber == True:
            StartingNumbers.append((CurrentNumberIndex-1)-NumberLocation)
            ContainsNumber = False
            NumberLocation = -1
        else:
            StartingNumbers.append(0)
        
            
    for i in range(100):
        print(StartingNumbers[i])
    return StartingNumbers[2019]

def main():
    t_start = time()
    
    StartingNumbers = ReadInFile()
    Answer = PlayGame(StartingNumbers)
    
    print("Part 1: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
