"""
Puzzle #6a - AdventOfCode
Read in customs answers
Determine how many questions were answered at least once per group
Sum that number for each group and output the total
"""
import math

def ReadInFile():
    File = open("./CustomsAnswers.txt", "r")
    CustomsAnswers = []

    Buffer = ""
    for Entry in File:
        if Entry =="\n":
            CustomsAnswers.append(Buffer)
            Buffer = ""
        else:
            Buffer += Entry.rstrip()
    CustomsAnswers.append(Buffer)

    return CustomsAnswers

def ParseCustomsAnswers(CustomsAnswers):
    GroupResponses = []

    for Group in CustomsAnswers:
        UniqueResponses = []
        for Answer in Group:
            if Answer not in UniqueResponses:
                UniqueResponses.append(Answer)
        GroupResponses.append(len(UniqueResponses))
        
    return GroupResponses

def SumResponses(GroupResponses):
    Result = 0
    for Response in GroupResponses:
        Result += Response

    return Result
                
def main():
    CustomsAnswers = ReadInFile()
    GroupResponses = ParseCustomsAnswers(CustomsAnswers)
    Answer = SumResponses(GroupResponses)

    print("The sum is ", Answer)

if __name__ == "__main__":
    main()
