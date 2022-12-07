"""
Puzzle #9a - AdventOfCode
Using answer from part 1 determine contiguous number sequence in input that sums
to the answer and output the sum of the two ends of those contiguous numbers

"""
import math

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    EncodedData = []

    for Entry in File:
        EncodedData.append(int(Entry))
            
    return EncodedData

def DetermineInvalidNumber(EncodedData, PreambleLength):
    LastIndex= PreambleLength
    FirstIndex = 0
    RelevantSet = EncodedData[FirstIndex:LastIndex]
    NumberToCheck = EncodedData[LastIndex]
    NumberToCheckFound = False

    for Data in EncodedData:
        for FirstValue in RelevantSet:
            for SecondValue in RelevantSet:
                if FirstValue != SecondValue:
                    Result = FirstValue + SecondValue
                    if Result == NumberToCheck:
                        NumberToCheckFound = True
                        break
            if NumberToCheckFound == True:
                break
        
        if NumberToCheckFound == True:
            LastIndex += 1
            FirstIndex +=1
            RelevantSet = EncodedData[FirstIndex:LastIndex]
            if LastIndex + 1 < len(EncodedData):
                NumberToCheck = EncodedData[LastIndex]
            NumberToCheckFound = False

        else:
            return NumberToCheck

def DetermineContiguousSet(EncodedData, InvalidNumber):
    FinalIndex = len(EncodedData)-1
    SetSize = 2
    FoundSet = False
    FirstValue = -1
    LastValue = -1
    Answer = -1
    FirstIndex = 0
    LastIndex= FirstIndex + SetSize
    RelevantSet = EncodedData[FirstIndex:LastIndex]

    while FoundSet == False:
        Result = 0
        for Elements in RelevantSet:
            Result += Elements
        if Result == InvalidNumber:
            RelevantSet.sort()
            FirstValue = RelevantSet[0]
            LastValue = RelevantSet[-1]
            Answer = FirstValue + LastValue
            FoundSet = True
            continue

        if LastIndex == FinalIndex:
            SetSize += 1
            FirstIndex = 0
            LastIndex = FirstIndex + SetSize

        else:
            FirstIndex +=1
            LastIndex +=1

        RelevantSet = EncodedData[FirstIndex:LastIndex]
        Result = 0

    return Answer
                
        

def main():
    EncodedData = ReadInFile()
    InvalidNumber = DetermineInvalidNumber(EncodedData, 25)
    print("Part 1: ", InvalidNumber)
    Answer = DetermineContiguousSet(EncodedData, InvalidNumber)
    print("Part 2",Answer)

if __name__ == "__main__":
    main()
