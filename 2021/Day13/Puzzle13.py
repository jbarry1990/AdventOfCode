def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    break_point = file_contents.index("\n")
    section_one = file_contents[0:break_point]
    section_two = file_contents[break_point +1:]
    
    points = []
    instructions = []

    for line in section_one:
        point = line.strip("\n").split(",")
        points.append([int(point[0]), int(point[1])])

    for line in section_two:
        instructions.append(line.strip("\n").split(" ")[2])

    return points , instructions
def ConstructGrid(points):
    #determine grid size
    width = 0
    length = 0
    grid = []

    for x,y in points:
        if x > width:
            width = x
        if y > length:
            length = y
    #create default grid
    for row in range(length+1):
        grid.append(["." for x in range(width+1)])

    # add points on grid
    for x,y in points:
        grid[y][x] = "#"
        
    return grid

def FoldGrid(grid, instruction):
    fold_line = int(instruction.split("=")[1])
    overlay = []
    underlay = []
    
    # fold up
    if instruction.startswith("y"):
        overlay = reversed(grid[fold_line+1:])
        underlay = grid[0:fold_line]        

    #fold left
    else:
        for row in grid:
            overlay.append(reversed(row[fold_line+1:]))
            underlay.append(row[0:fold_line])
        
    for row_index, row in enumerate(overlay):
        for column_index, column in enumerate(row):
            if column == "#":
                underlay[row_index][column_index] = "#"

    return underlay

def CountPoints(grid):
    count = 0
    for row in grid:
        for column in row:
            if column == "#":
                count +=1

    return count

def PartASolve(points, instructions):
    grid = ConstructGrid(points)
    grid = FoldGrid(grid, instructions[0])
    
    return CountPoints(grid)
            
def PartBSolve(points, instructions):
    grid = ConstructGrid(points)
    for instruction in instructions:
        grid = FoldGrid(grid, instruction)
    for row in grid:
        print("".join(row))
    
    return CountPoints(grid)

def main():
    file_contents = ReadFile("Inputs.txt")
    points, instructions = ParseFile(file_contents)
    answer = PartASolve(points, instructions)
    print("Part A Answer: ", answer)
    answer = PartBSolve(points, instructions)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
