"""
Puzzle #10a - AdventOfCode
Read in joltage values sort in ascending order. Determine how many differences of 1 there are and how many differences of 3 there are between each element
Make sure to count 0 for the source and MAX + 3 for the built in joltage of the device
output the product of the two difference counts

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
