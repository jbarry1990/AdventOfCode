import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content
           
def PartASolve(file_contents):
    rolling = []
    square = []
    new_rolling = []
    for r,line in enumerate(file_contents):
        for c,ch in enumerate(line):
            if ch == "O":
                rolling.append((r,c))
            elif ch == "#":
                square.append((r,c))

    for rock in rolling:
        r,c = rock
        while True:
            if r == 0:
                new_rolling.append((r,c))
                break
            
            elif (r-1,c) in new_rolling or (r-1,c) in square:
                new_rolling.append((r,c))
                break
            else:
                r-=1
    rowsort = []
    for i in range(len(file_contents)):
        group = []
        for r,c in new_rolling:
            if r == i:
                group.append((r,c))
        rowsort.append(group)

    max_score = len(file_contents)
    total = 0
    for i,row in enumerate(rowsort):
        total += (max_score-i)*len(row)
        
    return total

def PartBSolve(file_contents):
    cycles = 1000000000
    rolling = []
    square = []
    new_rolling = []
    for r,line in enumerate(file_contents):
        for c,ch in enumerate(line):
            if ch == "O":
                rolling.append((r,c))
            elif ch == "#":
                square.append((r,c))

    seen = dict()
    key = ",".join(map(str,rolling))
    seen[key] = [0,rolling]
    count = 0
    repeat = -1
    locations = None
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    while count < cycles:
        for i,j in directions:
            if i == -1 or j == -1:
                rolling.sort()
            else:
                rolling.sort(reverse=True)
            new_rolling = []
            for rock in rolling:
                r,c = rock
                
                while True:
                    if (r == 0 and i == -1) or (r == len(file_contents)-1 and i == 1) or (c == 0 and j == -1) or (c == len(file_contents[0])-1 and j == 1):
                        new_rolling.append((r,c))
                        break
                    
                    elif (r+i,c+j) in new_rolling or (r+i,c+j) in square:
                        new_rolling.append((r,c))
                        break
                    elif i == -1:
                        r-=1
                    elif i == 1:
                        r+=1
                    elif j == -1:
                        c-=1
                    elif j == 1:
                        c+=1
            rolling = new_rolling.copy()
            rolling.sort()
        key = ",".join(map(str,rolling))
        count +=1
        if key in seen:
            repeat = count,seen[key]
            break
        else:
            seen[key] = [count,rolling]
    
    mod = repeat[0]-repeat[1][0]
    found_it = ((cycles-repeat[1][0])%mod)+repeat[1][0]

    final_configuration = None
    for k,v in seen.items():
        if v[0] == found_it:
            final_configuration = v[1]
            break
    rowsort = []
    for i in range(len(file_contents)):
        group = []
        for r,c in final_configuration:
            if r == i:
                group.append((r,c))
        rowsort.append(group)

    max_score = len(file_contents)
    total = 0
    for i,row in enumerate(rowsort):
        total += (max_score-i)*len(row)
        
    return total

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
