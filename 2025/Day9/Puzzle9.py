def ReadInputs():
    File = open("./Inputs.txt", "r")
    results = [line.strip().split(",") for line in File]
    results = [[int(num) for num in nums] for nums in results]
    return results

def solveA(Input):
    areas = []
    for i,[x1,y1] in enumerate(Input):
        for [x2,y2] in Input[i+1:]:
            areas.append((abs(x2-x1)+1)*(abs(y2-y1)+1))
    return max(areas)
                
def solveB(Input):

    edges = []
    horizontal = []
    areas = []
    p1 = Input[0]

    for i in range(1,len(Input)+1):
        p2 = Input[i%len(Input)]
        x1,y1 = p1
        x2,y2 = p2
        edges.append(p1)

        if x1-x2 == 0:
            if y1 < y2:
                for i in range(1,(y2-y1)):
                    edges.append([x1,y1+i])
            else:
                for i in range(1,(y1-y2)):
                    edges.append([x1,y1-i])
        elif y1-y2 == 0:
            horizontal.append(p1)
            if x1 < x2:
                for i in range(1,(x2-x1)):
                    edges.append([x1+i,y1])
                    horizontal.append([x1+i,y1])
            else:
                for i in range(1,(x1-x2)):
                    edges.append([x1-i,y1])
                    horizontal.append([x1-i,y1])
            horizontal.append(p2)
        p1=p2
        
    shape = edges.copy()

    x_min = min(x for x,y in edges)
    x_max = max(x for x,y in edges)
    y_min = min(y for x,y in edges)
    y_max = max(y for x,y in edges)

    def check(point):
        [x,y]=point
        count = 0
        for xx in range(1,x_max+1):
            if [x+xx,y] in horizontal:
                break
            if [x+xx,y] in edges:
                count += 1
        return count

    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):
            if [x,y] in edges:
                continue
            if check([x,y])%2 != 0:
                shape.append([x,y])                

    for i,[x1,y1] in enumerate(Input):
        for [x2,y2] in Input[i+1:]:
            Valid = True
            if x1<x2 and y1<y2:
                for i in range(x1,x2+1):
                    for j in range(y1,y2+1):
                        if [i,j] not in shape:
                            Valid = False
                            break
                    if not Valid:
                        break

            elif x1>x2 and y1>y2:
                for i in range(x2,x1+1):
                    for j in range(y2,y1+1):
                        if [i,j] not in shape:
                            Valid = False
                            break
                    if not Valid:
                        break

            elif x1<x2 and y1>y2:
                for i in range(x1,x2+1):
                    for j in range(y2,y1+1):
                        if [i,j] not in shape:
                            Valid = False
                            break
                    if not Valid:
                        break
                            
            elif x1>x2 and y1<y2:
                for i in range(x2,x1+1):
                    for j in range(y1,y2+1):
                        if [i,j] not in shape:
                            Valid = False
                            break
                    if not Valid:
                        break

            if Valid:
                areas.append((abs(x2-x1)+1)*(abs(y2-y1)+1))
                
    return max(areas)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
