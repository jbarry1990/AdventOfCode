"""
Puzzle #9a - AdventOfCode
Read in encrypted data
Determine the first value in the list that isn't the product of a sum of the last 25 numbers
Output that value
"""
import math

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    EncodedData = []

    for Entry in File:
        EncodedData.append(int(Entry))
            
    return EncodedData

def ParseEncodedData(EncodedData, PreambleLength):
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

def main():
    EncodedData = ReadInFile()
    Answer = ParseEncodedData(EncodedData, 25)
    print("The first wrong number is: ", Answer)

if __name__ == "__main__":
    main()
