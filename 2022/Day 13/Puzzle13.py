from functools import cmp_to_key
def ReadInputs():
    File = open("./Inputs.txt", "r")
    Data = File.read().strip()
    Groups = []
    for Group in Data.split("\n\n"):
        Packet1, Packet2 = Group.split("\n")
        Groups.append([eval(Packet1), eval(Packet2)])

    return Groups

def Compare(Packet1, Packet2):
    if isinstance(Packet1, int) and isinstance(Packet2, int):
        if Packet1 < Packet2:
            return -1
        elif Packet1 > Packet2:
            return 1
        else:
            return 0
    elif isinstance(Packet1, list) and isinstance(Packet2, list):
        Index = 0
        while Index < len(Packet1) and Index < len(Packet2):
            Result = Compare(Packet1[Index], Packet2[Index])
            if Result == -1:
                return -1
            if Result == 1:
                return 1
            Index +=1

        if len(Packet1) == Index and len(Packet2) > Index:
            return -1
        elif len(Packet2) == Index and len(Packet1) > Index:
            return 1
        else:
            return 0
    elif isinstance(Packet1, int) and isinstance(Packet2, list):
        return Compare([Packet1], Packet2)
    else: 
        return Compare(Packet1, [Packet2])

def solveA(Groups):
    Answer = 0
    for Index, Group in enumerate(Groups):
        Packet1, Packet2 = [Packet for Packet in Group]
        Result = Compare(Packet1, Packet2)
        if Result == -1:
            Answer += Index+1

    return Answer

def solveB(Groups):
    Answer = 1
    Packets = []
    for Index, Group in enumerate(Groups):
        Packet1, Packet2 = [Packet for Packet in Group]
        Packets.append(Packet1)
        Packets.append(Packet2)

    Packets.append([[2]])
    Packets.append([[6]])

    Packets = sorted(Packets, key=cmp_to_key(lambda Packet1, Packet2: Compare(Packet1, Packet2)))

    for Index,Packet in enumerate(Packets):
        if Packet == [[2]] or Packet == [[6]]:
            Answer *= Index+1

    return Answer

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
