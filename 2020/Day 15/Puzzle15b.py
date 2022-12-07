"""
Puzzle #15b - AdventOfCode
Read in starting numbers. If the last number has been said before then the next number is the turn you are on - the turn the number was said on before. If it hasn't been said before
The next number is 0. Determine what the 30000000th number spoken will be. 
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    StartingNumbers = []

    for Entry in File:
        for Number in Entry.split(","):
            StartingNumbers.append(int(Number))
        
    return StartingNumbers

def PlayGame(StartingNumbers,EndGameOnNumber):
    NumberHasBeenSeen = {}

    for Index,Number in enumerate(StartingNumbers,1):
        NumberHasBeenSeen[Number] = Index
        
    for CurrentNumberIndex in range(len(StartingNumbers),EndGameOnNumber):
        LastSpoken = StartingNumbers[CurrentNumberIndex-1]

        if LastSpoken in NumberHasBeenSeen:
            LastInstance = NumberHasBeenSeen[LastSpoken]
            if LastInstance != CurrentNumberIndex:
                StartingNumbers.append(CurrentNumberIndex-LastInstance)
                NumberHasBeenSeen[LastSpoken] = CurrentNumberIndex
                continue

        StartingNumbers.append(0)
        NumberHasBeenSeen[LastSpoken] = CurrentNumberIndex
        
    return StartingNumbers[EndGameOnNumber-1]

def main():
    t_start = time()
    
    StartingNumbers = ReadInFile()
    Part1=2020
    Part2 = 30000000
    
    Answer = PlayGame(StartingNumbers, Part2)
    
    print("Part 1: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
