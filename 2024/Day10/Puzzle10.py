from collections import defaultdict

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def PartASolve(inputs):
    grid = [input.strip() for input in inputs]

    xmin = 0
    ymin = 0
    xmax = len(grid)
    ymax = len(grid[0])
    counts = []

    starts = []

    for x,row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "0":
                starts.append((x,y))

    for x,y in starts:
        count = 0
        queue = []
        visited = set()
        queue.append(((x,y),int(grid[x][y])))

        while len(queue) > 0:
            (r,c),value = queue.pop(0)

            if value == 9:
                if (r,c) not in visited:
                    count +=1
                    visited.add((r,c))
                    continue
            
            for i in range(4):
                dx,dy = [(-1,0),(0,1),(1,0),(0,-1)][i]
                nx = r+dx
                ny = c+dy
                nv = value+1
                
                if xmin <= nx < xmax and ymin <= ny < ymax and int(grid[nx][ny]) == nv:
                    queue.insert(0,((nx,ny),nv))
        counts.append(count)
    return sum(counts)
def PartBSolve(inputs):
    grid = [input.strip() for input in inputs]

    xmin = 0
    ymin = 0
    xmax = len(grid)
    ymax = len(grid[0])
    counts = []

    starts = []

    for x,row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "0":
                starts.append((x,y))

    for x,y in starts:
        count = 0
        queue = []
        visited = set()
        queue.append(((x,y),int(grid[x][y])))

        while len(queue) > 0:
            (r,c),value = queue.pop(0)

            if value == 9:
                count +=1
                continue
            
            for i in range(4):
                dx,dy = [(-1,0),(0,1),(1,0),(0,-1)][i]
                nx = r+dx
                ny = c+dy
                nv = value+1
                
                if xmin <= nx < xmax and ymin <= ny < ymax and int(grid[nx][ny]) == nv:
                    queue.insert(0,((nx,ny),nv))
        counts.append(count)
    return sum(counts)

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
