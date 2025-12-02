from collections import deque

def ReadFile(filename):
    with open(filename, "r") as f:
        content1 = f.readlines()
    with open(filename, "r") as f:
        content2 = f.read().strip()
        
    return content1,content2

def PartASolve(inputs1):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    grid = [line.strip() for line in inputs1]
    X = len(grid)
    Y = len(grid[0])
    start = None
    end = None
    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "S":
                start = (x,y)
            if col == "E":
                end = (x,y)
    Q = deque()
    visited = []
    Q.append(start)

    while Q:
        cx,cy = Q.popleft()

        if (cx,cy) in visited:
            continue
        visited.append((cx,cy))

        if (cx,cy) == end:
            break

        for i in range(4):
            dx,dy = dirs[i]
            nx = cx+dx
            ny = cy+dy

            if 0 <= nx < X and 0 <= ny < Y and (nx,ny) not in visited and grid[nx][ny] != "#":
                Q.append((nx,ny))

    track_length = len(visited)
    shortcuts = 0
    for i,track in enumerate(visited):
        x,y = track
        for j in range(4):
            dx,dy = dirs[j]

            nx = x+dx
            ny = y+dy
            nx2 = nx+dx
            ny2 = ny+dy

            if 0 <= nx < X and 0 <= ny < Y and grid[nx][ny] == "#":
                if 0 <= nx2 < X and 0 <= ny2 < Y and (nx2,ny2) in visited:
                    ni = visited.index((nx2,ny2))
                    if i < ni:
                        ps = ni-i-2
                        if ps >= 100:
                            shortcuts +=1
                            
    return shortcuts

def PartBSolve(inputs2):
    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    G = inputs2.split('\n')
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]

    for r in range(R):
        for c in range(C):
            if G[r][c] == 'S':
                sr,sc = r,c
            if G[r][c] == 'E':
                er,ec = r,c

    DIST = {}
    Q = deque([(0,er,ec)])
    while Q:
        d,r,c = Q.popleft()
        if (r,c) in DIST:
            continue
        DIST[(r,c)] = d
        for dr,dc in DIRS:
            rr,cc = r+dr, c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
                Q.append((d+1,rr,cc))

    def find_cheat(d0, CHEAT_TIME):
        ans = set()
        Q = deque([(0,None,None,None,sr,sc)])
        SEEN = set()
        SAVE = 100
        while Q:
            d,cheat_start,cheat_end,cheat_time,r,c = Q.popleft()
            assert cheat_end is None
            if d>=d0-SAVE:
                continue
            if G[r][c] == 'E':
                if cheat_end is None:
                    cheat_end = (r,c)
                if d<=d0-SAVE and (cheat_start,cheat_end) not in ans:
                    #print(d,d0,r,c,cheat_start,cheat_end,cheat_time)
                    ans.add((cheat_start, cheat_end))
            if (r,c,cheat_start,cheat_end,cheat_time) in SEEN:
                continue
            SEEN.add((r,c,cheat_start,cheat_end,cheat_time))
            #if len(SEEN) % 1000000 == 0:
            #    print(len(SEEN))

            if cheat_start is None: # start cheat
                assert G[r][c] != '#'
                Q.append((d,(r,c),None,CHEAT_TIME,r,c))
            if cheat_time is not None and G[r][c]!='#': # and cheat_time==0: # end cheat
                assert G[r][c] in ['.', 'S', 'E']
                if DIST[(r,c)] <= d0-100-d:
                    ans.add((cheat_start, (r,c)))
                    #if len(ans) % 1000 == 0:
                    #    print(len(ans), d+DIST[(r,c)])
                #Q.append((d,cheat_start,(r,c),None,r,c))
            if cheat_time == 0:
                continue
            else:
                for dr,dc in DIRS:
                    rr,cc = r+dr, c+dc
                    if cheat_time is not None:
                        assert cheat_time > 0
                        if 0<=rr<R and 0<=cc<C:
                            Q.append((d+1,cheat_start,None,cheat_time-1,rr,cc))
                    else:
                        if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
                            Q.append((d+1,cheat_start,cheat_end,cheat_time,rr,cc))
        #print(len(SEEN))
        return len(ans)

    d0 = DIST[(sr,sc)]
    print(find_cheat(d0, 2))
    print(find_cheat(d0, 20))
    return

def main():
    inputs1,inputs2 = ReadFile("Inputs.txt")
    answer = PartASolve(inputs1)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs2)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
