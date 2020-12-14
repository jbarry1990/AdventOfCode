"""
Puzzle #14a - AdventOfCode
Read in a mask and data value pairs for that mask. This will repeat for many entries
Using the mask manipulate the values and store them in the given memory addresses.
Sum the data in all the memory locations
Output the result
"""

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    BitMaskData = []
    BitMaskSpecific =[]

    for Index,Entry in enumerate(File):
        if Index == 0:
            BitMaskSpecific.append(Entry.strip())
        else:
            if Entry.startswith("mask"):
                BitMaskData.append(BitMaskSpecific)
                BitMaskSpecific = []
                BitMaskSpecific.append(Entry.strip())
                
            else:
                BitMaskSpecific.append(Entry.strip())
        BitMaskData.append(BitMaskSpecific)
                
    return BitMaskData

def RunInitialization(BitMaskData):
    Memory={}
    for BitMask in BitMaskData:
        Mask = ""
        MemoryAddress = 0
        MemoryValue = 0
        NewMemoryValue = ""
        for Index, Data in enumerate(BitMask):
            if Index == 0:
                Mask = Data[7:]
            else:
                MemoryAddress = Data[4:Data.find("]")]
                MemoryValue = int(Data[Data.find("=")+2:])
                MemoryValue = format(MemoryValue, "036b")

                for Index,Bit in enumerate(MemoryValue):
                    if Mask[Index] != "X":
                        NewMemoryValue += Mask[Index]
                    else:
                        NewMemoryValue += MemoryValue[Index]
                    Memory[MemoryAddress] = int(NewMemoryValue,2)

            NewMemoryValue = ""
    print(Memory)
    return Memory

def SumMemoryValues(Memory):
    Result = 0
    for Key in Memory:
        Result += Memory[Key]
        
    return Result

def main():
    BitMaskData = ReadInFile()
    Memory = RunInitialization(BitMaskData)
    Answer = SumMemoryValues(Memory)
    
    print("Part 1: ", Answer)

if __name__ == "__main__":
    main()
