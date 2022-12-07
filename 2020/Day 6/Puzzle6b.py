"""
Puzzle #6b - AdventOfCode
Read in customs answers
Determine how many questions were answered by everyone in the group
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
            Buffer += Entry
    CustomsAnswers.append(Buffer + "\n")

    return CustomsAnswers

def ParseCustomsAnswers(CustomsAnswers):
    GroupResponses = []
    for Group in CustomsAnswers:
        GroupSize = 0
        for Answers in Group:
            if Answers == "\n":
                GroupSize += 1

        EverybodyResponded = []
        for Answers in Group:
            if Group.count(Answers) == GroupSize and Answers not in EverybodyResponded and Answers != "\n":
                EverybodyResponded.append(Answers)
        GroupResponses.append(len(EverybodyResponded))
        
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
