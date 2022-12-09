def ReadInputs():
    File = open("./Inputs.txt", "r")
    ElfPairs = []
    
    for Line in File:
        NewLine = Line.replace("-", ",").strip()
        ElfPairs.append(NewLine.split(","))
    ElfPairsInt = []
    for Pairs in ElfPairs:
        Numbers = [int(s) for s in Pairs]
        ElfPairsInt.append(Numbers)

    return ElfPairsInt
    
def solveA(ElfPairs):
    count = 0
    for Pair in ElfPairs:
        if (Pair[0] <= Pair[2] and Pair[1]>=Pair[3]) or (Pair[2]<= Pair[0] and Pair[3]>=Pair[1]):
            count += 1
    return count

def solveB(ElfPairs): 
    count = 0
    for Pair in ElfPairs:
        if (Pair[0] <= Pair[2] <= Pair[1]) or (Pair[0] <= Pair[3]  <= Pair[1]) or (Pair[2] <= Pair[0] <= Pair[3]) or (Pair[2] <= Pair[1] <= Pair[3]):
            count +=1
    return count
def main():

    Inputs=ReadInputs()
    Part1=solveA(Inputs)
    print("Answer: ", Part1)
    Part2=solveB(Inputs)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
