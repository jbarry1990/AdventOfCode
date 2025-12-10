def ReadInputs():
    File = open("./Inputs.txt", "r")
    results = [line.strip().split(",") for line in File]
    results = [[int(num) for num in nums] for nums in results]
    return results

def solveA(Input):
    def calculate_distance(pair):
        [x1,y1,z1] = pair[0]
        [x2,y2,z2] = pair[1]
        return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

    pairs = []
    for i,p1 in enumerate(Input):
        for j,p2 in enumerate(Input[i+1:]):
           pairs.append([p1, p2])

    pairs = sorted(pairs, key=calculate_distance)

    circuit = []
    for i in range(1000):
        j1 = pairs[i][0]
        j2 = pairs[i][1]
        ij1 = -1
        ij2 = -1
        for x,c in enumerate(circuit):
            if j1 in c:
                ij1 = x
            if j2 in c:
                ij2 = x

        if ij1 == -1 and ij2 == -1:
            circuit.append([j1,j2])
        elif ij1 == -1 and ij2 != -1:
            circuit[ij2].append(j1)
        elif ij1 != -1 and ij2 == -1:
            circuit[ij1].append(j2)
        elif ij1 != ij2:
            for c in circuit[ij2]:
                circuit[ij1].append(c)
            del circuit[ij2]
            
        
    circuit = sorted(circuit, key=len, reverse=True)
    
    sizes = [len(c) for c in circuit[:3]]

    res = 1
    for s in sizes:
        res*=s
    return res

def solveB(Input):
    print(len(Input))
    def calculate_distance(pair):
        [x1,y1,z1] = pair[0]
        [x2,y2,z2] = pair[1]
        return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

    pairs = []
    for i,p1 in enumerate(Input):
        for j,p2 in enumerate(Input[i+1:]):
           pairs.append([p1, p2])

    pairs = sorted(pairs, key=calculate_distance)

    circuit = []
    for i in range(len(pairs)):
        j1 = pairs[i][0]
        j2 = pairs[i][1]
        ij1 = -1
        ij2 = -1
        for x,c in enumerate(circuit):
            if j1 in c:
                ij1 = x
            if j2 in c:
                ij2 = x

        if ij1 == -1 and ij2 == -1:
            circuit.append([j1,j2])
        elif ij1 == -1 and ij2 != -1:
            circuit[ij2].append(j1)
        elif ij1 != -1 and ij2 == -1:
            circuit[ij1].append(j2)
        elif ij1 != ij2:
            for c in circuit[ij2]:
                circuit[ij1].append(c)
            del circuit[ij2]

        if len(circuit) == 1 and len(circuit[0]) == len(Input):
            print(j1,j2)
            print(circuit)
            return j1[0]*j2[0]

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
