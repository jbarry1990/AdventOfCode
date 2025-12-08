from functools import cache

def ReadInputs():
    File = open("./Inputs.txt", "r")
    start = []
    end = 0
    splitters = []
    for row,line in enumerate(File):
        end +=1
        for col,char in enumerate(line):
            if char == "S":
                start.append([row,col])
            elif char == "^":
                splitters.append([row,col])
    return [start, end, splitters]
        
    
def solveA(Input):
    start = Input[0]
    end = Input[1]
    splitters = Input[2]
    beams = start
    count = 0
    for i in range(end):
        new_beams = []
        for x,beam in enumerate(beams):
            row,col = beam
            if [row+1,col] not in splitters:
                beams[x] = [row+1,col]
            else:
                count += 1
                new_beams.append([row+1,col+1])
                beams[x] = [row+1,col-1]
        if new_beams != []:
            beams += new_beams
        beams = list(map(list, set(map(tuple, beams))))
                
    return count
    
def solveB(Input):
    
    sr,sc = Input[0][0]
    end = Input[1]
    splitters = Input[2]

    @cache
    def score(r,c,end):
        if r+1 == end:
            return 1

        if [r+1,c] in splitters:
           return score(r+1,c+1,end)+score(r+1,c-1,end)
        else:
           return score(r+1,c,end)

    return score(sr,sc,end)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
