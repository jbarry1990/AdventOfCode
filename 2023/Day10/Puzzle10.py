import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
    
def Move(current_pos,current_direction,pipe):
    r,c = current_pos
    if pipe == "|":
        if current_direction == "U":
            current_direction = "U"
            current_pos = (r-1,c)
        else:
            current_direction = "D"
            current_pos = (r+1,c)
    elif pipe == "-":
        if current_direction == "L":
            current_direction = "L"
            current_pos = (r,c-1)
        else:
            current_direction = "R"
            current_pos = (r,c+1)
    elif pipe == "L":
        if current_direction == "D":
            current_direction = "R"
            current_pos = (r,c+1)
        else:
            current_direction = "U"
            current_pos = (r-1,c)
    elif pipe == "J":
        if current_direction == "D":
            current_direction = "L"
            current_pos = (r,c-1)
        else:
            current_direction = "U"
            current_pos = (r-1,c)
    elif pipe == "7":
        if current_direction == "R":
            current_direction = "D"
            current_pos = (r+1,c)
        else:
            current_direction = "L"
            current_pos = (r,c-1)
    elif pipe == "F":
        if current_direction == "L":
            current_direction = "D"
            current_pos = (r+1,c)
        else:
            current_direction = "R"
            current_pos = (r,c+1)
    return current_pos, current_direction

def PartASolve(file_contents):
    
    starting_loc = None
    starting_direction = "R"

    for i,row in enumerate(file_contents):
        for j,col in enumerate(row):
            if file_contents[i][j] == "S":
                starting_loc = (i,j)
                break
            if starting_loc != None:
                break
    loop = set()
    current_location = starting_loc
    current_direction = starting_direction
    count = 0
##    print("Starting Location: ",current_location)
##    print("Starting Direction: ",current_direction)
    while True:
        r,c = current_location
        pipe = file_contents[r][c]
        if pipe == "S":
            pipe = "-"
        current_location,current_direction = Move(current_location,current_direction,pipe)
        loop.add(current_location)
        count +=1
##        print("Current Location: ",current_location)
##        print("Current Direction: ",current_direction)
##        print("Count: ", count)
        if current_location == starting_loc:
            break

    if count%2==0:
        return count/2,loop
    else:
        return (count//2)+1,loop

def PartBSolve(file_contents,loop):
    S = "-"
    file_contents = [row.replace("S", S) for row in file_contents]
    file_contents = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(file_contents)]

    outside = set()

    for r, row in enumerate(file_contents):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))
                
    return len(file_contents) * len(file_contents[0]) - len(outside | loop)

def main():
    file_contents = ReadFile("Inputs.txt")
    answer,loop = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents,loop)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
