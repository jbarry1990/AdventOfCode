def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    grid = []
    for line in file_contents:
        row = [int(x) for x in line.strip("\n")]
        grid.append(row)
    return grid

def GetValue(grid, point):
    if point[0] < 0 or point[0] >= len(grid):
        return -1
    if point[1] < 0 or point[1] >= len(grid[0]):
        return -1
    return grid[point[0]][point[1]]

def PartASolve(grid, steps):
    width = len(grid[0])
    length = len(grid)
    offsets = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    count = 0

    # iterate over the desired number of steps
    for step in range(steps):
        flash = []
        # iterate over the grid to increase the power level. Add 
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                grid[row_index][col_index] += 1
                if col == 9:
                    flash.append([row_index, col_index])
                    count += 1
        # if a flash happens handle it
        while len(flash) > 0:
            for point in flash:
                for x,y in offsets:
                    adj_point = [point[0]+x, point[1]+y]
                    adj_value = GetValue(grid, adj_point)

                    if adj_value == -1:
                        continue
                    if adj_value == 9:
                        flash.append(adj_point)
                        count += 1
                    grid[adj_point[0]][adj_point[1]] += 1
                flash.remove(point)

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col > 9:
                    grid[row_index][col_index] = 0

    return count

def PartBSolve(grid, steps):
    width = len(grid[0])
    length = len(grid)
    offsets = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    step_count = 0
    AllFlashed = False

    # iterate over the desired number of steps
    while not AllFlashed:
        step_count += 1
        flash = []
        # iterate over the grid to increase the power level. Add 
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                grid[row_index][col_index] += 1
                if col == 9:
                    flash.append([row_index, col_index])
        # if a flash happens handle it
        while len(flash) > 0:
            for point in flash:
                for x,y in offsets:
                    adj_point = [point[0]+x, point[1]+y]
                    adj_value = GetValue(grid, adj_point)

                    if adj_value == -1:
                        continue
                    if adj_value == 9:
                        flash.append(adj_point)
                    grid[adj_point[0]][adj_point[1]] += 1
                flash.remove(point)

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col > 9:
                    grid[row_index][col_index] = 0

        occur = 0                  
        for row in grid:
            occur += row.count(0)

        if occur == 100:
            AllFlashed = True
    
    return step_count

def main():
    file_contents = ReadFile("Inputs.txt")
    grid = ParseFile(file_contents)
    answer = PartASolve(grid, 100)
    print("Part A Answer: ", answer)
    grid = ParseFile(file_contents)
    answer = PartBSolve(grid, 100)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
