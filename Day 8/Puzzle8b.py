"""
Puzzle #8b - AdventOfCode
Read in instruction set
Change only 1 jmp or nop instruction set to nop or jmp respectively
Run Instruction set to verify fix
Output accumulator value at the end of the Instruction Set
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
    FinalInstruction = len(InstructionSet)-1

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
            return False, Accumulator
        elif Index > FinalInstruction:
            KeepRunning = False
            return True, Accumulator
        else:
            PreviousInstructions.append(Index)
    return True, Accumulator

def ModifyInstructions(InstructionSet):
    AlreadyTried = []
    InstructionSetCopy = InstructionSet[:]
    Result = False
    Accumulator = 0

    for Index, Instruction in enumerate(InstructionSetCopy):
        if Instruction[0] == "jmp" and Instruction not in AlreadyTried:
            AlreadyTried.append(Instruction)
            
            TempList = list(Instruction)
            TempList[0] = "nop"
            Instruction = tuple(TempList)
            InstructionSetCopy[Index] = Instruction

            Result, Accumulator = RunInstructions(InstructionSetCopy)

        elif Instruction[0] == "nop" and Instruction not in AlreadyTried:
            AlreadyTried.append(Instruction)
            
            TempList = list(Instruction)
            TempList[0] = "jmp"
            Instruction = tuple(TempList)
            InstructionSetCopy[Index] = Instruction

            Result, Accumulator = RunInstructions(InstructionSetCopy)

        if Result == False:
            InstructionSetCopy = InstructionSet[:]

        else:
            break
            
            
    return Accumulator 
                
def main():
    InstructionSet = ReadInFile()
    Answer = ModifyInstructions(InstructionSet)
    print("Accumulator Value after program runs: ", Answer)

if __name__ == "__main__":
    main()
