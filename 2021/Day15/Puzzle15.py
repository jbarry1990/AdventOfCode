def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    risk_levels = {}
    end = (len(file_contents)-1, len(file_contents[0].strip())-1)
            

    grid = []
    for line in file_contents:
        row = [int(x) for x in line.strip("\n")]
        grid.append(row)

    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            risk_levels[row_index,column_index] = column
    
    return risk_levels, end

def RoutePath(start, visited, risk_levels, end, risk_points):
    offsets = [[0,1], [0,-1],[1,0],[-1,0]]

    if start == end:
        risk_points += risk_levels[end]
        return risk_points

    visited.append(start)

    for x,y in offsets:
        new_point = (start[0]+x, start[1] +y)
        if new_point not in risk_levels.keys() or new_point in visited:
            continue

        RoutePath(new_point, visited, risk_levels, end, risk_points)
        risk_points += risk_levels[new_point]
        if new_point in visited:
            visited.remove(new_point)
        
    
def PartASolve(risk_levels, end):
    visited = []
    risk_points = 0
    RoutePath((0,0), visited, risk_levels, end, risk_points)
    
    return
            
def PartBSolve(risk_levels, end):
    return

def main():
    file_contents = ReadFile("Inputs.txt")
    risk_levels, end = ParseFile(file_contents)
    answer = PartASolve(risk_levels, end)
    print("Part A Answer: ", answer)
    answer = PartBSolve(risk_levels,end)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
