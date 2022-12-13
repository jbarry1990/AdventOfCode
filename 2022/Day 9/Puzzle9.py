def ReadInputs():
        File = open("./Inputs.txt", "r")

        Steps = [Line.strip().split() for Line in File]

        for Index,Step in enumerate(Steps):
            Steps[Index][1] = int(Step[1])

        return Steps

def solveA(Steps):

    Visited = {}
    HeadCoordinates = [0,0]
    TailCoordinates = [0,0]


    for Step in Steps:
        if Step[0] == "R":
            for i in range(Step[1]):
                HeadCoordinates[0] +=1
                if HeadCoordinates[1] == TailCoordinates[1]:
                    if abs(HeadCoordinates[0] - TailCoordinates[0]) == 2:
                        TailCoordinates[0] +=1
                        if TailCoordinates in Visited:
                            Visited[TailCoordinates] +=1
                        else:
                            Visited[TailCoordinates] = 1
                else:
                    



        elif Step[0] == "L":
            for i in range(Step[1]):
                HeadCoordinates[0] -=1

        elif Step[0] == "U":
            for i in range(Step[1]):
                HeadCoordinates[1] +=1

        elif Step[0] == "D":
            for i in range(Step[1]):
                HeadCoordinates[1] -=1

    print(HeadCoordinates)
    return

def solveB(Input):
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
