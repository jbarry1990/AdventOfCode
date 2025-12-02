from collections import deque, defaultdict

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def PartASolve(inputs):
    grid =[x.strip() for x in inputs]
    xmin = 0
    ymin = 0
    xmax = len(grid)
    ymax = len(grid[0])
    plants = defaultdict(list)
    ranges = defaultdict(list)
    
    for x,row in enumerate(grid):
        for y, col in enumerate(row):
            plants[col].append((x,y))

    for plant in plants:
        seen = set()
        for loc in plants[plant]:
            if loc in seen:
                continue
            else:
                seen.add(loc)

            queue = []
            visited = set()
            queue.append(loc)

            while len(queue) > 0:
                x,y = queue.pop(0)
                visited.add((x,y))

                for i in range(4):
                    dx,dy = [(1,0),(-1,0),(0,1),(0,-1)][i]

                    nx=x+dx
                    ny=y+dy

                    if xmin <= nx < xmax and ymin <= ny < ymax and grid[nx][ny] == plant and (nx,ny) not in visited:
                        queue.append((nx,ny))
                        seen.add((nx,ny))
            ranges[plant].append(list(visited))
    prices = []
    for plant in ranges:
        for areas in ranges[plant]:
            area = len(areas)
            perimeter = 0
            for x,y in areas:
                for i in range(4):
                    dx,dy = [(1,0),(-1,0),(0,1),(0,-1)][i]

                    nx=x+dx
                    ny=y+dy

                    if xmin <= nx < xmax and ymin <= ny < ymax:
                        if grid[nx][ny] != plant:
                            perimeter +=1
                    else:
                        perimeter +=1
            prices.append(perimeter*area)
    return sum(prices)
                
            
        
    

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
