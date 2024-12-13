
def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content
        
def PartASolve(grid):
    visited = set()
    grid = [x.strip() for x in grid]
    row_min = 0
    row_max = len(grid)
    col_min = 0
    col_max = len(grid[0])
    obstacles = []
    location = (0,0)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    index = 0
    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "#":
                obstacles.append((x,y))
            elif col == "^":
                location = (x,y)
    InBounds = True
    visited.add(location)
    while InBounds:
        dx,dy = directions[index]
        lx,ly = location
        new_loc = (lx+dx, ly+dy)
        nx,ny = new_loc
        if row_min <= nx < row_max and col_min <= ny < col_max:
            if new_loc in obstacles:
                if index == 3:
                    index = 0
                else:
                    index +=1
            else:
                visited.add(new_loc)
                location = new_loc
        else:
            InBounds = False
        
    return len(visited)

def PartBSolve(grid):
    count = 0
    counter = 0
    grid = [x.strip() for x in grid]
    row_min = 0
    row_max = len(grid)
    col_min = 0
    col_max = len(grid[0])
    start = (0,0)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "^":
                start = (x,y)
               
    for x in range(row_max):
        for y in range(col_max):
            location = start
            
            if grid[x][y] == "^":
                continue

            InBounds = True
            visited = set()
            index = 0
            visited.add((location,index))
            
            while InBounds:
                dx,dy = directions[index]
                lx,ly = location
                nx,ny = (lx+dx, ly+dy)
                if row_min <= nx < row_max and col_min <= ny < col_max:
                    if grid[nx][ny] == "#" or (nx == x and ny == y):
                        if index == 3:
                            index = 0
                        else:
                            index +=1
                    elif (nx,ny,index) in visited:
                        count += 1
                        InBounds = False
                    else:
                        visited.add((nx,ny,index))
                        location = (nx,ny)
                else:
                    InBounds = False
    return count

def main():
    grid = ReadFile("Inputs.txt")
    answer = PartASolve(grid)
    print("Part A Answer: ", answer)
    answer = PartBSolve(grid)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
