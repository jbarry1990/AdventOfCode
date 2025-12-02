from collections import defaultdict, deque

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
        return content

def PartASolve(inputs):
    grids = inputs.split("\n\n")

    keys = []
    locks = []
    height = 0
    for grid in grids:
        grid = grid.split("\n")
        height = len(grid)
        counts = []
        for i in range(len(grid[0])):
            count = 0
            for j in range(len(grid)):
                if grid[j][i] == "#":
                    count +=1
            counts.append(count)
        
        if all(x == "#" for x in grid[0]):
            locks.append(counts)
        else:
            keys.append(counts)


    total = 0
    for lock in locks:
        for key in keys:
            result = [x+y for x,y in zip(lock,key)]
            if all(x <= 7 for x in result):
                total +=1
    return total
            
                
                
                
        
        
        
def PartBSolve(inputs):
    return
             
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
