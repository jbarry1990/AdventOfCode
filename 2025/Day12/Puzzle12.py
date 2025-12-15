def ReadInputs():
    File = open("./Inputs.txt", "r")
    Lines = File.read().split("\n\n")
    patterns = {int(key):value.split("\n") for key,value in (pattern.split(":\n") for pattern in Lines[:-1])}
    plots = [[size,allocation.split()] for size,allocation in (plot.split(": ") for plot in Lines[-1].split("\n"))]
    plots = [[size,[int(a) for a in allocation]] for size,allocation in plots]

    return [plots,patterns]

    
def solveA(Input):
    count = 0
    plots = Input[0]
    patterns = Input[1]

    areas = [[int(a),int(b)] for a,b in (plot[0].split("x") for plot in plots)]
    spots = [b for a,b in(plot for plot in plots)]
    counts = [sum(spot) for spot in spots]
    for i,[a,b] in enumerate(areas):
        if (a//3)*(b//3) >= counts[i]:
            count+=1
    return count
    

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
