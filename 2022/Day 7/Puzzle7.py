def ReadInputs():
        File = open("./Inputs.txt", "r")

        Commands = [Command.strip() for Command in File]

        return Commands   

def solveA(Commands):
    Path = []
    DirectorySize = {}
    for Command in Commands:
        Words = Command.split()

        if Words[1] == "cd":
            if Words[2] == "..":
                Path.pop()
            else:
                Path.append(Words[2])
        elif Words[1] == "ls":
            continue
        elif Words[0] == "dir":
            continue
        else:
            Size = int(Words[0])
            for i in range(len(Path)):
                Key = "/".join(Path[:i+1])
                if Key in DirectorySize:
                    DirectorySize[Key]+=Size
                else:
                    DirectorySize[Key] = Size

    Answer = 0
    for Key, Value in DirectorySize.items():
        if Value <= 100000:
            Answer += Value

    return Answer, DirectorySize

def solveB(DirectorySize):
    MaxSize = 70000000
    MinSpace = 30000000
    CurrentSize = DirectorySize["/"]
    RemainingSize = MaxSize-CurrentSize
    Threshold = MinSpace-RemainingSize

    CanBeDeleted = []
    for Key,Value in DirectorySize.items():
        if Value >= Threshold:
            CanBeDeleted.append(Value)
        
    return min(CanBeDeleted)

def main():

    Input=ReadInputs()
    Part1,DirectorySize=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(DirectorySize)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
