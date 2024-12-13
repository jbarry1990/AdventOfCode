import sys
sys.setrecursionlimit(10000)

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
    
##def DFS(node,path,result,end_node):
##    if node == end_node:
##        result.append(path)
##
##    r,c = node
##    if graph[r][c] in slopes:
##        dr,dc = slopes[graph[r][c]]
##        if (r+dr,c+dc) in path:
##            pass
##        else:
##            DFS((r+dr,c+dc),path + [(r+dr,c+dc)],result,end_node)
##    else:
##        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
##            if 0 <= r+dr < len(graph) and 0 <= c+dc < len(graph[0]) and (r+dr,c+dc) not in path and graph[r+dr][c+dc] != "#":
##
##                DFS((r+dr,c+dc),path + [(r+dr,c+dc)],result,end_node)

seen = set()

def dfs(pt):
    end = (len(grid) - 1, grid[-1].index("."))
    if pt == end:
        return 0

    m = -float("inf")

    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx) + graph[pt][nx])
    seen.remove(pt)

    return m
                
##def PartASolve(file_contents):
##    global graph
##    graph = file_contents
##    global slopes
##    slopes = {"<":(0,-1), ">":(0,1), "^":(-1,0), "v":(1,0)}
##
##    result = []
##    end_node = (len(graph)-1,len(graph[0])-2)
##                
##    DFS((0,1),[],result,end_node)
##
##    return max(len(x) for x in result)


def PartBSolve(file_contents):
    global grid
    grid = file_contents

    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[-1].index("."))

    points = [start, end]

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                continue
            neighbors = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))
    global graph

    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()
            
            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))



    print(dfs(start))

def main():
    file_contents = ReadFile("Inputs.txt")
##    answer = PartASolve(file_contents)
##    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
