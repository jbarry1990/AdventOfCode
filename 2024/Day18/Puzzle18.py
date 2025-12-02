from collections import deque
import heapq

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
    return content

def PartASolve(inputs):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    size = 71
    kilobytes = []
    coordinates = inputs.split("\n")
    for coordinate in coordinates:
        x,y = coordinate.split(",")
        kilobytes.append((int(x),int(y)))
    grid = [["." for _ in range(size)] for _ in range(size)]

    for i in range(1024):
        x,y = kilobytes[i]
        grid[y][x] = "#"
        
    Q = deque()
    sx,sy = 0,0
    ex,ey = 70,70
    scores = []
    visited = set((0,0))
    Q.append((0,0,0))

    while Q:
        x,y,s = Q.popleft()
        if (x,y) == (ex,ey):
            scores.append(s)
            continue
        
        if (x,y) in visited:
            continue
        visited.add((x,y))

        for i in range(4):
            dx,dy = dirs[i]
            nx = x+dx
            ny = y+dy
            if 0 <= nx < size and 0 <= ny < size and (nx,ny) not in visited and grid[ny][nx] != "#":
                Q.append((nx,ny,s+1))
        
    return min(scores)

def PartBSolve(inputs):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    size = 71
    kilobytes = []
    coordinates = inputs.split("\n")
    for coordinate in coordinates:
        x,y = coordinate.split(",")
        kilobytes.append((int(x),int(y)))
    grid = [["." for _ in range(size)] for _ in range(size)]

    for i in range(1024):
        x,y = kilobytes[i]
        grid[y][x] = "#"
        
    for i in range(1024,len(kilobytes)):
        gx,gy = kilobytes[i]

        grid[gy][gx] = "#"
        
        Q = deque()
        sx,sy = 0,0
        ex,ey = 70,70
        scores = []
        visited = set((0,0))
        Q.append((0,0,0))

        while Q:
            x,y,s = Q.popleft()
            if (x,y) == (ex,ey):
                scores.append(s)
                continue
            
            if (x,y) in visited:
                continue
            visited.add((x,y))

            for i in range(4):
                dx,dy = dirs[i]
                nx = x+dx
                ny = y+dy
                if 0 <= nx < size and 0 <= ny < size and (nx,ny) not in visited and grid[ny][nx] != "#":
                    Q.append((nx,ny,s+1))
        
        if len(scores) == 0:
            return(str(gx)+","+str(gy))

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
