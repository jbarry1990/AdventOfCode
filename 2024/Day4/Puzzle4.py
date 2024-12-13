
def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        formatted = []
        for line in content:
            formatted.append(line.strip())
        return formatted
    


def PartASolve(file_contents):
    count = 0
    x_max = len(file_contents)
    y_max = len(file_contents[0])
    x_loc = []
    for x,line in enumerate(file_contents):
        for y,char in enumerate(line):
            if char == "X":
                x_loc.append((x,y))

    for x,y in x_loc:
        if y-3 >= 0:
            if file_contents[x][y-1] == "M" and file_contents[x][y-2] == "A" and file_contents[x][y-3] == "S":
                count +=1
        if y+3 < y_max:
            if file_contents[x][y+1] == "M" and file_contents[x][y+2] == "A" and file_contents[x][y+3] == "S":
                count +=1
        if x-3 >= 0:
            if file_contents[x-1][y] == "M" and file_contents[x-2][y] == "A" and file_contents[x-3][y] == "S":
                count +=1
        if x+3 < x_max:
            if file_contents[x+1][y] == "M" and file_contents[x+2][y] == "A" and file_contents[x+3][y] == "S":
                count +=1
        if x-3 >= 0 and y-3 >= 0:
            if file_contents[x-1][y-1] == "M" and file_contents[x-2][y-2] == "A" and file_contents[x-3][y-3] == "S":
                count +=1
        if x+3 < x_max and y+3 < y_max:
            if file_contents[x+1][y+1] == "M" and file_contents[x+2][y+2] == "A" and file_contents[x+3][y+3] == "S":
                count +=1
        if x-3 >=0 and y+3 < y_max:
            if file_contents[x-1][y+1] == "M" and file_contents[x-2][y+2] == "A" and file_contents[x-3][y+3] == "S":
                count +=1
        if x+3 < x_max and y-3 >= 0:
            if file_contents[x+1][y-1] == "M" and file_contents[x+2][y-2] == "A" and file_contents[x+3][y-3] == "S":
                count +=1

    return count
    

def PartBSolve(file_contents):
    count = 0
    x_max = len(file_contents)
    y_max = len(file_contents[0])
    a_loc = []
    for x,line in enumerate(file_contents):
        for y,char in enumerate(line):
            if char == "A":
                a_loc.append((x,y))

    for x,y in a_loc:
        if x-1 >= 0 and y-1 >= 0 and x+1 < x_max and y+1 < y_max and x-1 >=0 and y+1 < y_max and x+1 < x_max and y-1 >= 0:
            if ((file_contents[x-1][y-1] == "M" and file_contents[x+1][y+1] == "S") or (file_contents[x-1][y-1] == "S" and file_contents[x+1][y+1] == "M")) and ((file_contents[x-1][y+1] == "M" and file_contents[x+1][y-1] == "S") or (file_contents[x-1][y+1] == "S" and file_contents[x+1][y-1] == "M")):
                count +=1

    return count

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
