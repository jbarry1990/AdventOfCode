from collections import deque
import heapq

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    return content
            
def PartASolve(inputs):
    grid = [x.strip() for x in inputs]
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    index = 1
    start = None
    end = None
    walls = []
    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "S":
                start = (x,y)
            if col == "E":
                end = (x,y)
            if col == "#":
                walls.append((x,y))
    x,y = start
    dx,dy = dirs[index]
    Q = []
    visited = set()
    heapq.heappush(Q,(0,x,y,index))
    best = []

    while Q:

        score,cx,cy,i = heapq.heappop(Q)
        
        if (cx,cy) == end:
            best.append(score)
            continue
        
        if (cx,cy,i) in visited:
            continue
        visited.add((cx,cy,i))

        cdx,cdy = dirs[i]
        nx = cx+cdx
        ny = cy+cdy
        if (nx,ny) not in walls:
            heapq.heappush(Q,(score+1,nx,ny,i))

        heapq.heappush(Q,(score+1000,cx,cy,(i+1)%4))
        heapq.heappush(Q,(score+1000,cx,cy,(i+3)%4))
        
    print(best)
    return best

def PartBSolve(inputs):
    grid = [x.strip() for x in inputs]
    R = len(grid)
    C = len(grid[0])
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    index = 1
    start = None
    end = None
    walls = []
    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "S":
                start = (x,y)
            if col == "E":
                end = (x,y)
            if col == "#":
                walls.append((x,y))
    x,y = start
    dx,dy = dirs[index]
    Q = []
    DIST = {}
    heapq.heappush(Q,(0,x,y,index,set()))
    best = None

    while Q:

        score,cx,cy,i,visited = heapq.heappop(Q)
        if (cx,cy,i) not in DIST:
            DIST[(cx,cy,i)] = score
        
        if (cx,cy) == end and best == None:
            best = score
            continue
        
        if (cx,cy,i) in visited:
            continue
        visited.add((cx,cy,i))

        cdx,cdy = dirs[i]
        nx = cx+cdx
        ny = cy+cdy
        if (nx,ny) not in walls:
            heapq.heappush(Q,(score+1,nx,ny,i,visited))

        heapq.heappush(Q,(score+1000,cx,cy,(i+1)%4,visited))
        heapq.heappush(Q,(score+1000,cx,cy,(i+3)%4,visited))
        
    Q = []
    er,ec = end
    SEEN = set()
    for dir in range(4):
        heapq.heappush(Q, (0,er,ec,dir))
    DIST2 = {}
    while Q:
        d,r,c,dir = heapq.heappop(Q)
        if (r,c,dir) not in DIST2:
            DIST2[(r,c,dir)] = d
        if (r,c,dir) in SEEN:
            continue
        SEEN.add((r,c,dir))
        # going backwards instead of forwards here
        dr,dc = dirs[(dir+2)%4]
        rr,cc = r+dr,c+dc
        if 0<=cc<C and 0<=rr<R and grid[rr][cc] != '#':
            heapq.heappush(Q, (d+1, rr,cc,dir))
        heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
        heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

    OK = set()
    for r in range(R):
        for c in range(C):
            for dir in range(4):
                # (r,c,dir) is on an optimal path if the distance from start to end equals the distance from start to (r,c,dir) plus the distance from (r,c,dir) to end.
                if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                    OK.add((r,c))
    print(len(OK))
        
def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
