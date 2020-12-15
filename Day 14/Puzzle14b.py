"""
Puzzle #14a - AdventOfCode
Read in a mask and data value pairs for that mask. This will repeat for many entries
Using the mask manipulate the values and store them in the given memory addresses.
Sum the data in all the memory locations
Output the result
"""
from time import time
def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    BitMaskData = []
    BitMaskSpecific =[]
    Count = 0
    for Index,Entry in enumerate(File):
        Count +=1
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

def DetermineMasks(Mask):
    Masks =[]
    Locations = []

    for Index, Bit in enumerate(Mask):
        if Bit == "X":
            Locations.append(Index)

    NumberOfX = len(Locations)
    NumberOfVariations = 2**NumberOfX

    Variations = []
    for BinaryNumber in range(0,NumberOfVariations):
        Variations.append(format(BinaryNumber, "0" + str(NumberOfX) + "b"))
        
    NewMask = list(Mask)
    for Variation in Variations:
        for Index, Location in enumerate(Locations):
            NewMask[Location] = Variation[Index]
        Masks.append("".join(NewMask))
 
    return Masks

def RunInitialization(BitMaskData):
    Memory = {}
    for BitMask in BitMaskData:
        Mask = ""
        MemoryAddress = 0
        MemoryValue = 0
        NewMemoryAddress = ""
        for Index, Data in enumerate(BitMask):
            if Index == 0:
                Mask = Data[7:]
            else:
                MemoryAddress = int(Data[4:Data.find("]")])
                MemoryAddress = format(MemoryAddress, "036b")
                MemoryValue = int(Data[Data.find("=")+2:])
                for Index,Bit in enumerate(Mask):
                    if Bit == "1":
                        NewMemoryAddress += "1"
                    elif Bit == "0":
                        NewMemoryAddress += MemoryAddress[Index]
                    elif Bit == "X":
                        NewMemoryAddress += "X"

                Masks = DetermineMasks(NewMemoryAddress)
                for Iteration in Masks:
                    Memory[int(Iteration,2)] = MemoryValue    
                NewMemoryAddress = ""

    return Memory

def SumMemoryValues(Memory):        
    return sum(Memory.values())

def main():
    t_start = time()
    
    BitMaskData = ReadInFile()
    Memory = RunInitialization(BitMaskData)
    Answer = SumMemoryValues(Memory)
    
    print("Part 2: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
