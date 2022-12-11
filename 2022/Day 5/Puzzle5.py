def ReadInputs():
        File = open("./Inputs.txt", "r")

        Input = File.read().split("\n\n")
        Map = Input[0].split("\n")
        Instructions = Input[1].split("\n")

        return Map, Instructions
    
def solveA(Map, Instructions):
    Stacks = {int(digit):[] for digit in Map[-1].replace(" ","")}

    Indexes = [index for index,char in enumerate(Map[-1]) if(char != " ")]

    {Stacks[i+1].append(Line[Index]) for Line in reversed(Map[:-1]) for i,Index in enumerate(Indexes) if Line[Index] != " "}
    
    for Instruction in Instructions:
        Instruction = Instruction.replace("move ","").replace("from ","").replace("to ","").strip().split()
        Instruction = [int(i) for i in Instruction]

        crates = Instruction[0]
        From = Instruction[1]
        To = Instruction[2]

        for crate in range(crates):
            Removed = Stacks[From].pop()
            Stacks[To].append(Removed)
    

    Answer = ""
    for Stack in Stacks:
        Answer += Stacks[Stack][-1]
    return Answer

def solveB(Map, Instructions):
    Stacks = {int(digit):[] for digit in Map[-1].replace(" ","")}

    Indexes = [index for index,char in enumerate(Map[-1]) if(char != " ")]

    {Stacks[i+1].append(Line[Index]) for Line in reversed(Map[:-1]) for i,Index in enumerate(Indexes) if Line[Index] != " "}
    
    for Instruction in Instructions:
        Instruction = Instruction.replace("move ","").replace("from ","").replace("to ","").strip().split()
        Instruction = [int(i) for i in Instruction]

        crates = Instruction[0]
        From = Instruction[1]
        To = Instruction[2]

        Removed = []
        for crate in range(crates):
            Removed.insert(0,Stacks[From].pop())
        for Item in Removed:
            Stacks[To].append(Item)
    

    Answer = ""
    for Stack in Stacks:
        Answer += Stacks[Stack][-1]
    return Answer

def main():

    Map, Instructions=ReadInputs()
    Part1=solveA(Map, Instructions)
    print("Answer: ", Part1)
    Part2=solveB(Map, Instructions)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
