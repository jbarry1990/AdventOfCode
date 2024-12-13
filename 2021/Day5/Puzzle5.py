def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content

def ParseFile(file_contents):
    segments = []
    new_string = []
    for line in file_contents:
        new_string.append(line.replace(" -> ", ",").strip("\n"))

    for line in new_string:
        segments.append(line.split(","))

    for line_index, segment in enumerate(segments):
        for position_index, number in enumerate(segment):   
            segments[line_index][position_index] = int(number)
    
    return segments

def PartASolve(segments):
    #filter on vertical or horizontal lines
    filtered_segments = []
    for segment in segments:
        if segment[0] != segment[2] and segment[1] != segment[3]:
            continue
        filtered_segments.append(segment)
        
    #determine range of grid from remaining data points
    MaxColumn = MaxRow = 0
    for segment in filtered_segments:
        if segment[0] > MaxColumn or segment[2] > MaxColumn:
            if segment[0] > segment[2]:
                MaxColumn = segment[0]
            else:
                MaxColumn = segment[2]
                
        if segment[1] > MaxRow or segment[3] > MaxRow:
            if segment[1] > segment[3]:
                MaxRow = segment[1]
            else:
                MaxRow = segment[3]

    #create a grid
    grid = []
    for index in range(0,MaxRow+1):
        grid.append([0 for column in range(0, MaxColumn+1)])

    #process data    
    for segment in filtered_segments:
        x1 = segment[0]
        y1 = segment[1]
        x2 = segment[2]
        y2 = segment[3]

        LowestY = y1 if y1 < y2 else y2
        LowestX = x1 if x1 < x2 else x2

        length = 0
        if x1 == x2:
            length = abs(y1-y2)
            for index in range(length+1):
                grid[LowestY+index][x1] += 1
        else:
            length = abs(x1-x2)
            for index in range(length+1):                
                grid[y1][LowestX+index] += 1

    count = 0
    for row in grid:
        for number in row:
            if number >= 2:
                count +=1

    return count

def PartBSolve(segments):
    #determine range of grid from remaining data points
    MaxColumn = MaxRow = 0
    for segment in segments:
        if segment[0] > MaxColumn or segment[2] > MaxColumn:
            if segment[0] > segment[2]:
                MaxColumn = segment[0]
            else:
                MaxColumn = segment[2]
                
        if segment[1] > MaxRow or segment[3] > MaxRow:
            if segment[1] > segment[3]:
                MaxRow = segment[1]
            else:
                MaxRow = segment[3]

    #create a grid
    grid = []
    for index in range(0,MaxRow+1):
        grid.append([0 for column in range(0, MaxColumn+1)])

    #process data    
    for segment in segments:
        x1 = segment[0]
        y1 = segment[1]
        x2 = segment[2]
        y2 = segment[3]

        LowestY = y1 if y1 < y2 else y2
        LowestX = x1 if x1 < x2 else x2

        length = 0
        if x1 == x2:
            length = abs(y1-y2)
            for index in range(length+1):
                grid[LowestY+index][x1] += 1
        elif y1 == y2:
            length = abs(x1-x2)
            for index in range(length+1):                
                grid[y1][LowestX+index] += 1
        elif x1 < x2 and y1 < y2:
            length = abs(x1-x2)
            for index in range(length+1):
                grid[y1+index][x1+index] +=1
            #add to x and add to y
        elif x1 < x2 and y1 > y2:
            length = abs(x1-x2)
            for index in range(length+1):
                grid[y1-index][x1+index] +=1
            #add to x and subtract from y
        elif x1 > x2 and y1 < y2:
            length = abs(x1-x2)
            for index in range(length+1):
                grid[y1+index][x1-index] +=1
            #subtract from x and add to y
        elif x1 > x2 and y1 > y2:
            length = abs(x1-x2)
            for index in range(length+1):
                grid[y1-index][x1-index] +=1
            #subtract from x and subtract from y

    count = 0
    for row in grid:
        for number in row:
            if number >= 2:
                count +=1

    return count

def main():
    file_contents = ReadFile("Inputs.txt")
    segments = ParseFile(file_contents)
    answer = PartASolve(segments)
    print("Part A Answer: ", answer)
    answer = PartBSolve(segments)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
