"""
Puzzle #8a - AdventOfCode
Read in instruction set
Follow rules until a rule is run a second time keeping track of accumulator value
Output accumulator value just before a duplicated line
"""
import math

def ReadInFile():
    File = open("./Instructions.txt", "r")
    InstructionSet = []

    for Entry in File:
        InstructionSet.append((Entry.split()[0], int(Entry.split()[1])))
            
    return InstructionSet

def RunInstructions(InstructionSet):
    Index = 0
    Accumulator = 0
    PreviousInstructions = []
    KeepRunning = True

    while KeepRunning:
        CurrentInstruction = InstructionSet[Index]

        if CurrentInstruction[0] == "nop":
            Index += 1
        elif CurrentInstruction[0] == "acc":
            Accumulator += CurrentInstruction[1]
            Index += 1
        elif CurrentInstruction[0] == "jmp":
            Index += CurrentInstruction[1]

        if Index in PreviousInstructions:
            KeepRunning = False
            return Accumulator
        else:
            PreviousInstructions.append(Index)
                
def main():
    InstructionSet = ReadInFile()
    Answer = RunInstructions(InstructionSet)
    print("Accumulator Value before infinite loop is: ", Answer)

if __name__ == "__main__":
    main()
