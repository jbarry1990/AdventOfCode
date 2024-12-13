import heapq
from heapq import heappush, heappop

def IsConsecutive(grandparent,parent,current,neighbor):
    r0,c0 = grandparent
    r1,c1 = parent
    r2,c2 = current
    r3,c3 = neighbor

    if (r0 == r1 == r2 == r3) or (c0 == c1 == c2 == c3):
        return True
    return False

def dijkstra(source):
    nodes={}
    queue=[(0,source,-1,-1)] #priority queue
    while queue:
        dist,node,dir_,num_dir =heapq.heappop(queue)
        if (node,dir_,num_dir) in nodes:
            continue

        nodes[node,dir_,num_dir] = dist
        
        for i, (dr,dc) in enumerate([(-1,0),(0,1),(1,0),(0,-1)]):
            r,c = node
            new_dir = i
            new_num_dir = (1 if new_dir != dir_ else num_dir+1)
            if InBounds(r+dr,c+dc) and new_num_dir <=10 and ((new_dir+2)%4 != dir_) and (new_dir ==dir_ or num_dir >= 4 or num_dir == -1):
                cost = int(graph[r+dr][c+dc])
                heapq.heappush(queue,(cost+dist,(r+dr,c+dc),new_dir,new_num_dir))
    return nodes

def dijkstraB(source):
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
            print(hl)
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        if n >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
    
def InBounds(r,c):
    h = len(graph)
    w = len(graph[0])
    if (0 <= r < h) and (0 <= c < w):
        return True
    return False

def PartASolve(file_contents):
    global graph
    graph = file_contents
    h = len(graph)
    w = len(graph[0])
                        
    nodes = dijkstra((0,0))

    answer = 1e9
    for (node,dir_,indir),v in nodes.items():
        r,c = node
        if r==w-1 and c==h-1:
            answer = min(answer,v)
    return answer

def PartBSolve(file_contents):
    global grid
    grid = [list(map(int, line.strip())) for line in file_contents]
    h = len(graph)
    w = len(graph[0])
                        
    nodes = dijkstraB((0,0))

    answer = 1e9
    for (node,dir_,indir),v in nodes.items():
        r,c = node
        if r==w-1 and c==h-1:
            answer = min(answer,v)
    return answer

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
