def ReadInputs():
        File = open("./Inputs.txt", "r")
        Numbers = []
        for Line in File:
            Numbers.append(int(Line.strip()))

        return Numbers
    
def solveA(Numbers):
    Decoded = [[i,x] for i,x in enumerate(Numbers)]

    for Index, Number in enumerate(Numbers):
        CurrentIndex = Decoded.index([Index,Number])
        NewIndex = (CurrentIndex + Number)%len(Numbers)
        
        #Move Left and index is higher insert then remove
        if CurrentIndex + Number < CurrentIndex and NewIndex > CurrentIndex:
            Decoded.insert(NewIndex, [NewIndex, Number])
            Decoded.remove([Index,Number])
        #move left and index is lower remove then insert
        elif CurrentIndex + Number < CurrentIndex and NewIndex < CurrentIndex:
            Decoded.remove([Index,Number])
            Decoded.insert(NewIndex, [NewIndex, Number])
        #move right and index is higher remove then insert
        elif CurrentIndex + Number > CurrentIndex and NewIndex > CurrentIndex:
            Decoded.remove([Index,Number])
            Decoded.insert(NewIndex, [NewIndex, Number])
        #move right and index is lower add one to index and insert then remove
        elif CurrentIndex + Number > CurrentIndex and NewIndex < CurrentIndex:
            Decoded.remove([Index,Number])
            Decoded.insert(NewIndex+1, [NewIndex+1, Number])

    ZeroIndex = -1
    for x,y in Decoded:
        if y == 0:
            ZeroIndex = Decoded.index([x,y])
    print(Decoded[(ZeroIndex+1000-1)%len(Numbers)][1])
    print(Decoded[(ZeroIndex+2000-1)%len(Numbers)][1])
    print(Decoded[(ZeroIndex+3000-1)%len(Numbers)][1])
    return Decoded[(ZeroIndex+1000)%len(Numbers)][1] + Decoded[(ZeroIndex+2000)%len(Numbers)][1] + Decoded[(ZeroIndex+3000)%len(Numbers)][1]

    


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
