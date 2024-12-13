import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    empty_rows = [i for i,r in enumerate(file_contents) if r.count(".")==len(r)]
    empty_columns = []
    for i in range(len(file_contents[0])):
        isEmpty = True
        for j in range(len(file_contents)):
            if file_contents[j][i] == "#":
                isEmpty = False
        if isEmpty:
            empty_columns.append(i)
        else:
            isEmpty = True
    
    empty_rows.reverse()
    for row in empty_rows:
        file_contents.insert(row, "."*len(file_contents[0]))

    empty_columns.reverse()
    for i,line in enumerate(file_contents):
        temp = list(line)
        for col in empty_columns:
            temp.insert(col,".")
            file_contents[i] = "".join(temp)
            
    locations = []
    for i,row in enumerate(file_contents):
        for j,col in enumerate(row):
            if file_contents[i][j] == "#":
                locations.append((i,j))
    distance = []
    while len(locations) !=0:
        r1,c1 = locations.pop()
        for r2,c2 in locations:
            if abs(r1-r2) == 0 and abs(c1-c2) == 0:
                continue
            distance.append(abs(r1-r2)+abs(c1-c2))
    
    return sum(distance)

def PartBSolve(file_contents):
    size = 1000000-1
    locations = []
    for i,row in enumerate(file_contents):
        for j,col in enumerate(row):
            if file_contents[i][j] == "#":
                locations.append((i,j))

    empty_rows = [i for i,r in enumerate(file_contents) if r.count(".")==len(r)]
    empty_columns = []
    for i in range(len(file_contents[0])):
        isEmpty = True
        for j in range(len(file_contents)):
            if file_contents[j][i] == "#":
                isEmpty = False
        if isEmpty:
            empty_columns.append(i)
        else:
            isEmpty = True

    empty_rows.reverse()
    for row in empty_rows:
        for i,loc in enumerate(locations):
            r,c = loc
            if r > row:
                locations[i] = (r+size,c)
    empty_columns.reverse()           
    for col in empty_columns:
        for i,loc in enumerate(locations):
            r,c = loc
            if c > col:
                locations[i] = (r,c+size)
    
    distance = []
    while len(locations) !=0:
        r1,c1 = locations.pop()
        for r2,c2 in locations:
            if abs(r1-r2) == 0 and abs(c1-c2) == 0:
                continue
            distance.append(abs(r1-r2)+abs(c1-c2))
    
    return sum(distance)

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    file_contents = ReadFile("Inputs.txt")
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
