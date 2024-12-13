def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    heightmap = []

    for line in file_contents:
        heightmap.append([int(digit) for digit in line.strip("\n")])

    return heightmap

def PartASolve(heightmap):

    heightmap_length = len(heightmap)
    heightmap_width = len(heightmap[0])

    low_points = []                      
    for row_index, row in enumerate(heightmap):
        for column_index, column in enumerate(row):
            #top lefthand corner
            if row_index ==0 and column_index == 0:
                if column < heightmap[row_index][column_index+1] and column <heightmap[row_index+1][column_index]:
                    low_points.append([row_index,column_index])
            #top righthand corner
            elif row_index ==0 and column_index == heightmap_width-1:
                if column < heightmap[row_index][column_index-1] and column <heightmap[row_index+1][column_index]:
                    low_points.append([row_index,column_index])
            #bottom righthand corner
            elif row_index ==heightmap_length-1 and column_index == heightmap_width-1:
                if column < heightmap[row_index][column_index-1] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])
            #bottom lefthand corner
            elif row_index ==heightmap_length-1 and column_index == 0:
                if column < heightmap[row_index][column_index+1] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])
            #top of map
            elif row_index == 0:
                if column < heightmap[row_index][column_index+1] and column < heightmap[row_index][column_index-1] and column <heightmap[row_index+1][column_index]:
                    low_points.append([row_index,column_index])
            #bottom of map
            elif row_index == heightmap_length-1:
                if column < heightmap[row_index][column_index+1] and column < heightmap[row_index][column_index-1] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])
            #left side of map
            elif column_index == 0:
                if column < heightmap[row_index][column_index+1] and column < heightmap[row_index+1][column_index] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])
            #right side of map
            elif column_index == heightmap_width-1:
                if column < heightmap[row_index][column_index-1] and column < heightmap[row_index+1][column_index] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])
            #middle of the map
            else:
                if column < heightmap[row_index][column_index+1] and column < heightmap[row_index][column_index-1] and column < heightmap[row_index+1][column_index] and column <heightmap[row_index-1][column_index]:
                    low_points.append([row_index,column_index])

    risk_level = []
    for point in low_points:
        risk_level.append(heightmap[point[0]][point[1]] +1)

    risk_rating = sum(risk_level)
            
    return risk_rating, low_points

def GetValue(heightmap, point):
    if point[0] < 0 or point[0] >= len(heightmap):
        return 10
    if point[1] < 0 or point[1] >= len(heightmap[0]):
        return 10
    return heightmap[point[0]][point[1]]

def PartBSolve(heightmap, low_points):
    basin_sizes = []
    offsets = [[0,1], [0, -1], [-1,0], [1,0]]
    checked_points = []
    #iterate through the low points found in part a
    for low_point in low_points:
        unchecked_points = [low_point]
        count = 1

        while len(unchecked_points) > 0:
            for point in unchecked_points:
                if point in checked_points:
                    continue

                for offset in offsets:
                    point_to_check = [point[0]+offset[0], point[1]+offset[1]]
                    value = GetValue(heightmap, point_to_check)
                    if value == 10:
                        continue
                    elif value == 9:
                        if point_to_check in checked_points:
                            continue
                        checked_points.append(point_to_check)
                    else:
                        if point_to_check in unchecked_points or point_to_check in checked_points:
                            continue 
                        unchecked_points.append(point_to_check)
                        count +=1
            
                unchecked_points.remove(point)
                checked_points.append(point)

        basin_sizes.append(count)

    basin_sizes.sort(reverse=True)
    multiplication = 1
    for index in range(3):
        multiplication *= basin_sizes[index]  
    return multiplication

def main():
    file_contents = ReadFile("Inputs.txt")
    heightmap = ParseFile(file_contents)
    answer, low_points = PartASolve(heightmap)
    print("Part A Answer: ", answer)
    answer = PartBSolve(heightmap, low_points)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
