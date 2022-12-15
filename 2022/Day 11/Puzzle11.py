import math

def ReadInputs():
    File = open("./Inputs.txt", "r")

    Input = File.read().strip()

    StartingItems = []
    Operations = []
    Divisible = []
    Whereto = []

    for Monkey in Input.split("\n\n"):
        ID, Items, Operation, Test, IfTrue, IfFalse = Monkey.split("\n")
        StartingItems.append([int(i) for i in Items.split(":")[1].split(",")])
        Words = Operation.split()
        Operations.append("".join(Words[-3:]))
        Divisible.append(int(Test.split()[-1]))
        Whereto.append([int(IfTrue.split()[-1]), int(IfFalse.split()[-1])])

    return StartingItems, Operations, Divisible, Whereto

def solveA(StartingItems, Operations, Divisible, Whereto):
    Count  = [0 for _ in range(len(StartingItems))]
    for _ in range(20):
        for i in range(len(StartingItems)):
            for Item in StartingItems[i]:
                Count[i] +=1
                old = Item
                Item = eval(Operations[i])
                Item = Item//3
                if Item % Divisible[i] == 0:
                    StartingItems[Whereto[i][0]].append(Item)
                else:
                    StartingItems[Whereto[i][1]].append(Item)
            StartingItems[i] = []

    return sorted(Count)[-1]*sorted(Count)[-2]

def solveB(StartingItems, Operations, Divisible, Whereto):
    LCM = 1
    for x in Divisible:
        LCM *= (LCM*x)

    Count  = [0 for _ in range(len(StartingItems))]
    for _ in range(10000):
        for i in range(len(StartingItems)):
            for Item in StartingItems[i]:
                Count[i] +=1
                old = Item
                Item = eval(Operations[i])
                Item = Item%LCM
                if Item % Divisible[i] == 0:
                    StartingItems[Whereto[i][0]].append(Item)
                else:
                    StartingItems[Whereto[i][1]].append(Item)
            StartingItems[i] = []

    return sorted(Count)[-1]*sorted(Count)[-2]

def main():

    StartingItems, Operations, Divisible, Whereto=ReadInputs()
    Part1=solveA(StartingItems, Operations, Divisible, Whereto)
    print("Answer: ", Part1)
    StartingItems, Operations, Divisible, Whereto=ReadInputs()
    Part2=solveB(StartingItems, Operations, Divisible, Whereto)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
