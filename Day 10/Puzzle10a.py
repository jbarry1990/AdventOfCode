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

def DetermineJoltageDifference(SortedReadings):
    OnesCount = 0
    ThreesCount = 0
    LastIndex = len(SortedReadings)-1

    for Index, Adapter in enumerate(SortedReadings):
        if Index == LastIndex:
            continue
        if SortedReadings[Index+1] - Adapter == 1:
            OnesCount += 1
        elif SortedReadings[Index+1] - Adapter == 3:
            ThreesCount += 1

    return OnesCount, ThreesCount
        
def main():
    JoltReadings = ReadInFile()
    SortedReadings = SortReadings(JoltReadings)
    OnesCount, ThreesCount = DetermineJoltageDifference(SortedReadings)
    print("Part 1: ", OnesCount*ThreesCount)


if __name__ == "__main__":
    main()
