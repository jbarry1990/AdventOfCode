"""
Puzzle #10b - AdventOfCode
Determine how many different pathways can be taken to get to the device.
An adapter can be removed if the difference between the adapter preceeding it and the adapter
succeeding it is 3 or less
"""
import math
from itertools import combinations

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    JoltReadings = []

    for Entry in File:
        JoltReadings.append(int(Entry))
            
    return JoltReadings

def SortReadings(JoltReadings):
    JoltReadings.append(0)
    JoltReadings.sort()
    JoltReadings.append(JoltReadings[-1]+3)

    return JoltReadings

def CalculateCombinations(SortedReadings):

    Path = [1]
    NumberOfAdapters = len(SortedReadings)

    for EndOfChain in range(1, NumberOfAdapters):
        Answer = 0
        for ElementsInPath in range(EndOfChain):
            if SortedReadings[ElementsInPath] + 3 >= SortedReadings[EndOfChain]:
                Answer += Path[ElementsInPath]
        Path.append(Answer)

    return Path[-1]       
        
def main():
    JoltReadings = ReadInFile()
    SortedReadings = SortReadings(JoltReadings)
    Answer = CalculateCombinations(SortedReadings)
    print("Part 2: ", Answer)


if __name__ == "__main__":
    main()
