def ReadInputs():
        File = open("./Inputs.txt", "r")
        Data = File.read().strip()
        Solved = {}
        Equations = {}
        for Line in Data.split("\n"):
            Words = Line.split()
            if len(Words) == 2:
                Solved[Words[0][:-1]] = int(Words[1])
            else:
                Equations[Words[0][:-1]] = " ".join(Words[1:])

        return Solved, Equations


    
def solveA(Solved, Equations):
    DeleteKeys = []
    while len(Equations) > 0:
        
        for Key in DeleteKeys:
             Equations.pop(Key)
        DeleteKeys = []

        for Key, Value in Equations.items():
            if Value[:4] in Solved and Value[-4:] in Solved:
                Equations[Key] = str(Solved[Value[:4]]) + str(Value[4:-4]) + str(Solved[Value[-4:]])
                Solved[Key] = eval(Equations[Key])
                DeleteKeys.append(Key)

    
    return int(Solved["root"])

def solveB(Solved, Equations):
    return

def main():

    Solved, Equations=ReadInputs()
    Part1=solveA(Solved, Equations)
    print("Answer: ", Part1)
    Part2=solveB(Solved,Equations)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
