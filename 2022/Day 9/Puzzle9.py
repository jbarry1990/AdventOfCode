Visited = set()
Knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
X = 0
Y = 1
Visited.add("0,0")

VisitedA = set()
KnotsA = [[0,0],[0,0]]
VisitedA.add("0,0")

def ReadInputs():
        File = open("./Inputs.txt", "r")

        Steps = [Line.strip().split() for Line in File]

        for Index,Step in enumerate(Steps):
            Steps[Index][1] = int(Step[1])

        return Steps

def MoveTail(Head, Tail, Index):                
    if Tail[X]+2 == Head[X] and Tail[Y]+1 == Head[Y]:
        Tail[X] +=1
        Tail[Y] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString) 
        return             
                        
    if Tail[X]+2 == Head[X] and Tail[Y]-1 == Head[Y]:
        Tail[X] +=1
        Tail[Y] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return           
                
    if Tail[X]-2 == Head[X] and Tail[Y]+1 == Head[Y]:
        Tail[X] -=1
        Tail[Y] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return
                    
    if Tail[X]-2 == Head[X] and Tail[Y]-1 == Head[Y]:
        Tail[X] -=1
        Tail[Y] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return
                
    if Tail[Y]+2 == Head[Y] and Tail[X]+1 == Head[X]:
        Tail[Y] +=1
        Tail[X] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[Y]+2 == Head[Y] and Tail[X]-1 == Head[X]:
        Tail[Y] +=1
        Tail[X] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)  
        return                  
                    
    if Tail[Y]-2 == Head[Y] and Tail[X]+1 == Head[X]:
        Tail[Y] -=1
        Tail[X] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return    
                        
    if Tail[Y]-2 == Head[Y] and Tail[X]-1 == Head[X]:
        Tail[Y] -=1
        Tail[X] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[Y]-2 == Head[Y] and Tail[X]-2 == Head[X]:
        Tail[Y] -=1
        Tail[X] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[Y]-2 == Head[Y] and Tail[X]+2 == Head[X]:
        Tail[Y] -=1
        Tail[X] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[Y]+2 == Head[Y] and Tail[X]-2 == Head[X]:
        Tail[Y] +=1
        Tail[X] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[Y]+2 == Head[Y] and Tail[X]+2 == Head[X]:
        Tail[Y] +=1
        Tail[X] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[X]-2 == Head[X] and Tail[Y]-2 == Head[Y]:
        Tail[X] -=1
        Tail[Y] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[X]-2 == Head[X] and Tail[Y]+2 == Head[Y]:
        Tail[X] -=1
        Tail[Y] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)

    if Tail[X]+2 == Head[X] and Tail[Y]-2 == Head[Y]:
        Tail[X] +=1
        Tail[Y] -=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Tail[X]+2 == Head[X] and Tail[Y]+2 == Head[Y]:
        Tail[X] +=1
        Tail[Y] +=1
        if Index+1 == len(Knots)-1:
            IndexString =  str(Tail[X]) + "," + str(Tail[Y])
            Visited.add(IndexString)
        return

    if Head[Y] == Tail[Y]:
        if Head[X] - Tail[X] == 2:
            Tail[X] +=1
            if Index+1 == len(Knots)-1:
                IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                Visited.add(IndexString)
            return

    if Head[X] == Tail[X]:
        if Head[Y] - Tail[Y] == -2:
            Tail[Y] -=1
            if Index+1 == len(Knots)-1:
                IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                Visited.add(IndexString) 
            return

    if Head[X] == Tail[X]:
        if Head[Y] - Tail[Y] == 2:
            Tail[Y] +=1
            if Index+1 == len(Knots)-1:
                IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                Visited.add(IndexString)
            return

    if Head[Y] == Tail[Y]:
        if Head[X] - Tail[X] == -2:
            Tail[X] -=1
            if Index+1 == len(Knots)-1:
                IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                Visited.add(IndexString)
            return

def solveA(Steps):
    Head = KnotsA[0]
    Tail = KnotsA[1]

    for Step in Steps:
        if Step[0] == "R":
            for i in range(Step[1]):
                Head[X] +=1
                if Head[Y] == Tail[Y]:
                    if abs(Head[X] - Tail[X]) == 2:
                        Tail[X] +=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        VisitedA.add(IndexString)
                            
                elif Tail[X]+2 == Head[X] and Tail[Y]+1 == Head[Y]:
                    Tail[X] +=1
                    Tail[Y] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                                    
                elif Tail[X]+2 == Head[X] and Tail[Y]-1 == Head[Y]:
                    Tail[X] +=1
                    Tail[Y] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                                    
        elif Step[0] == "L":
            for i in range(Step[1]):
                Head[X] -=1
                if Head[Y] == Tail[Y]:
                    if abs(Head[X] - Tail[X]) == 2:
                        Tail[X] -=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        VisitedA.add(IndexString)
                            
                elif Tail[X]-2 == Head[X] and Tail[Y]+1 == Head[Y]:
                    Tail[X] -=1
                    Tail[Y] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                            
                elif Tail[X]-2 == Head[X] and Tail[Y]-1 == Head[Y]:
                    Tail[X] -=1
                    Tail[Y] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                    
        elif Step[0] == "U":
            for i in range(Step[1]):
                Head[Y] +=1
                if Head[X] == Tail[X]:
                    if abs(Head[Y] - Tail[Y]) == 2:
                        Tail[Y] +=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        VisitedA.add(IndexString)
                            
                elif Tail[Y]+2 == Head[Y] and Tail[X]+1 == Head[X]:
                    Tail[Y] +=1
                    Tail[X] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                                    
                elif Tail[Y]+2 == Head[Y] and Tail[X]-1 == Head[X]:
                    Tail[Y] +=1
                    Tail[X] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)

        elif Step[0] == "D":
            for i in range(Step[1]):
                Head[Y] -=1
                if Head[X] == Tail[X]:
                    if abs(Head[Y] - Tail[Y]) == 2:
                        Tail[Y] -=1
                        IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                        VisitedA.add(IndexString)
                            
                elif Tail[Y]-2 == Head[Y] and Tail[X]+1 == Head[X]:
                    Tail[Y] -=1
                    Tail[X] +=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)
                                    
                elif Tail[Y]-2 == Head[Y] and Tail[X]-1 == Head[X]:
                    Tail[Y] -=1
                    Tail[X] -=1
                    IndexString =  str(Tail[X]) + "," + str(Tail[Y])
                    VisitedA.add(IndexString)

    return len(VisitedA)

def solveB(Steps):
    for Step in Steps:
        if Step[0] == "R":
            for i in range(Step[1]):
                for Index,Knot in enumerate(Knots):
                    if Index == len(Knots)-1:
                        break
                    Head = Knots[Index]
                    Tail = Knots[Index+1]
                    if Index == 0:
                        Head[X] +=1
                    MoveTail(Head, Tail, Index)
                                                    
        elif Step[0] == "L":
            for i in range(Step[1]):
                for Index,Knot in enumerate(Knots):
                    if Index == len(Knots)-1:
                        break
                    Head = Knots[Index]
                    Tail = Knots[Index+1]
                    if Index == 0:
                        Head[X] -=1
                    MoveTail(Head, Tail, Index)
                    
        elif Step[0] == "U":
            for i in range(Step[1]):
                for Index,Knot in enumerate(Knots):
                    if Index == len(Knots)-1:
                        break
                    Head = Knots[Index]
                    Tail = Knots[Index+1]
                    if Index == 0:
                        Head[Y] +=1
                    MoveTail(Head, Tail, Index)
                                        
        elif Step[0] == "D":
            for i in range(Step[1]):
                for Index,Knot in enumerate(Knots):
                    if Index == len(Knots)-1:
                        break
                    Head = Knots[Index]
                    Tail = Knots[Index+1]
                    if Index == 0:
                        Head[Y] -=1
                    MoveTail(Head, Tail, Index)                            

    return len(Visited)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
