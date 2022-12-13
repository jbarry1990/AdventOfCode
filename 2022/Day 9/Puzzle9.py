def ReadInputs():
        File = open("./Inputs.txt", "r")

        Steps = [Line.strip().split() for Line in File]

        for Index,Step in enumerate(Steps):
            Steps[Index][1] = int(Step[1])

        return Steps

def solveA(Steps):

    Visited = set()
    Head = [0,0]
    Tail = [0,0]
    X = 0
    Y = 1
    Visited.add(str(Tail[X])+","+str(Tail[Y]))


    Count = 0
    for Step in Steps:
        Count +=1
        if Step[0] == "R":
            for i in range(Step[1]):
                Head[X] +=1
                if Head[Y] == Tail[Y]:
                    if abs(Head[X] - Tail[X]) == 2:
                        Tail[X] +=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        Visited.add(IndexString)
                            
                elif Tail[X]+2 == Head[X] and Tail[Y]+1 == Head[Y]:
                    Tail[X] +=1
                    Tail[Y] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                                    
                elif Tail[X]+2 == Head[X] and Tail[Y]-1 == Head[Y]:
                    Tail[X] +=1
                    Tail[Y] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                                    
        elif Step[0] == "L":
            for i in range(Step[1]):
                Head[X] -=1
                if Head[Y] == Tail[Y]:
                    if abs(Head[X] - Tail[X]) == 2:
                        Tail[X] -=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        Visited.add(IndexString)
                            
                elif Tail[X]-2 == Head[X] and Tail[Y]+1 == Head[Y]:
                    Tail[X] -=1
                    Tail[Y] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                            
                elif Tail[X]-2 == Head[X] and Tail[Y]-1 == Head[Y]:
                    Tail[X] -=1
                    Tail[Y] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                    
        elif Step[0] == "U":
            for i in range(Step[1]):
                Head[Y] +=1
                if Head[X] == Tail[X]:
                    if abs(Head[Y] - Tail[Y]) == 2:
                        Tail[Y] +=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        Visited.add(IndexString)
                            
                elif Tail[Y]+2 == Head[Y] and Tail[X]+1 == Head[X]:
                    Tail[Y] +=1
                    Tail[X] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                                    
                elif Tail[Y]+2 == Head[Y] and Tail[X]-1 == Head[X]:
                    Tail[Y] +=1
                    Tail[X] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)

        elif Step[0] == "D":
            for i in range(Step[1]):
                Head[Y] -=1
                if Head[X] == Tail[X]:
                    if abs(Head[Y] - Tail[Y]) == 2:
                        Tail[Y] -=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        Visited.add(IndexString)
                            
                elif Tail[Y]-2 == Head[Y] and Tail[X]+1 == Head[X]:
                    Tail[Y] -=1
                    Tail[X] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)
                                    
                elif Tail[Y]-2 == Head[Y] and Tail[X]-1 == Head[X]:
                    Tail[Y] -=1
                    Tail[X] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    Visited.add(IndexString)

    return len(Visited)

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
