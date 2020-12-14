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

def DetermineMasks(Mask):
    #1. Store Location of X's in Mask in a list
    #2. Determine how many X's there are
    #3. Generate all possible combinations in binary
    #4. Apply all possible variations to the given Mask adding each new Mask to a list
    #5. Return list
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
        print("Variation: ", Variation)
        Index = 0
        for Number in Variation:
            for MaskIndex, Bit in enumerate(Mask):
                if MaskIndex == Locations[Index]:
                    NewMask[MaskIndex] = Number
            Index+=1
            
                
    return Masks
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
    return Memory

def SumMemoryValues(Memory):
    Result = 0
    for Key in Memory:
        Result += Memory[Key]
        
    return Result

def main():
    BitMaskData = ReadInFile()
    DetermineMasks("1001X0XX")
    #Memory = RunInitialization(BitMaskData)
    Answer = 0
    
    print("Part 1: ", Answer)

if __name__ == "__main__":
    main()
