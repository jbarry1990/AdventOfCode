import re

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip())
        return stripped_content

def InBounds(r,c,rd,cd):
    if (rd,cd) == (0,1) and c > len(grid[0])-1:
        return False
    elif (rd,cd) == (0,-1) and c < 0:
        return False
    elif (rd,cd) == (1,0) and r > len(grid)-1:
        return False
    elif (rd,cd) == (-1,0) and r < 0:
        return False
    else:
        return True

def PartASolve(file_contents):
    global grid
    grid = file_contents
    num_rows = len(grid)
    num_cols = len(grid[0])
    energized = set()
    row,col = (0,0)
    rowd,cold = (0,1)

    beam_positions = [(row,col,rowd,cold)]
    
    while len(beam_positions)is not 0:
        r,c,rd,cd = beam_positions.pop()
        if (r,c,rd,cd) in energized:
            continue
            
        while True:
            if (r,c,rd,cd) in energized:
                break
            else:
                energized.add((r,c,rd,cd))
                
            if grid[r][c] == "|" and (rd,cd) in [(0,1),(0,-1)]:
                if InBounds(r-1,c,-1,0):
                    beam_positions.append((r-1,c,-1,0))
                if InBounds(r+1,c,1,0):
                    beam_positions.append((r+1,c,1,0))
                break
            elif grid[r][c] == "-" and (rd,cd) in [(1,0),(-1,0)]:
                if InBounds(r,c-1,0,-1):
                    beam_positions.append((r,c-1,0,-1))
                if InBounds(r,c+1,0,1):
                    beam_positions.append((r,c+1,0,1))
                break
            elif (grid[r][c] == "\\" and (rd,cd) == (0,1)) or (grid[r][c] == "/" and (rd,cd) == (0,-1)):
                r+=1
                rd,cd = (1,0)
            elif (grid[r][c] == "\\" and (rd,cd) == (0,-1)) or (grid[r][c] == "/" and (rd,cd) == (0,1)):
                r-=1
                rd,cd = (-1,0)
            elif (grid[r][c] == "\\" and (rd,cd) == (1,0)) or (grid[r][c] == "/" and (rd,cd) == (-1,0)):
                c+=1
                rd,cd = (0,1)
            elif (grid[r][c] == "\\" and (rd,cd) == (-1,0)) or (grid[r][c] == "/" and (rd,cd) == (1,0)):
                c-=1
                rd,cd = (0,-1)
            else:
                r+=rd
                c+=cd

            if InBounds(r,c,rd,cd) == False:
                break
    sorted_el = list(energized)
    sorted_el.sort()
    unique = set()
    for a,b,c,d in sorted_el:
        unique.add((a,b))
    return len(unique)

def PartBSolve(file_contents):
    starts = []
    starts.append([(0,i) for i in range(len(grid))])
    starts.append([(len(grid)-1,i) for i in range(len(grid))])
    starts.append([(i,0) for i in range(len(grid[0]))])
    starts.append([(i,len(grid[0])-1) for i in range(len(grid[0]))])
    all_uniques = []
    for rowd,cold,i in [(1,0,0),(-1,0,1),(0,1,2),(0,-1,3)]:
        starting = starts[i]
        for row,col in starting:
            energized = set()
            beam_positions = [(row,col,rowd,cold)]
    
            while len(beam_positions) != 0:
                r,c,rd,cd = beam_positions.pop()
                if (r,c,rd,cd) in energized:
                    continue
                    
                while True:
                    if (r,c,rd,cd) in energized:
                        break
                    else:
                        energized.add((r,c,rd,cd))
                        
                    if grid[r][c] == "|" and (rd,cd) in [(0,1),(0,-1)]:
                        if InBounds(r-1,c,-1,0):
                            beam_positions.append((r-1,c,-1,0))
                        if InBounds(r+1,c,1,0):
                            beam_positions.append((r+1,c,1,0))
                        break
                    elif grid[r][c] == "-" and (rd,cd) in [(1,0),(-1,0)]:
                        if InBounds(r,c-1,0,-1):
                            beam_positions.append((r,c-1,0,-1))
                        if InBounds(r,c+1,0,1):
                            beam_positions.append((r,c+1,0,1))
                        break
                    elif (grid[r][c] == "\\" and (rd,cd) == (0,1)) or (grid[r][c] == "/" and (rd,cd) == (0,-1)):
                        r+=1
                        rd,cd = (1,0)
                    elif (grid[r][c] == "\\" and (rd,cd) == (0,-1)) or (grid[r][c] == "/" and (rd,cd) == (0,1)):
                        r-=1
                        rd,cd = (-1,0)
                    elif (grid[r][c] == "\\" and (rd,cd) == (1,0)) or (grid[r][c] == "/" and (rd,cd) == (-1,0)):
                        c+=1
                        rd,cd = (0,1)
                    elif (grid[r][c] == "\\" and (rd,cd) == (-1,0)) or (grid[r][c] == "/" and (rd,cd) == (1,0)):
                        c-=1
                        rd,cd = (0,-1)
                    else:
                        r+=rd
                        c+=cd

                    if InBounds(r,c,rd,cd) == False:
                        break
            sorted_el = list(energized)
            sorted_el.sort()
            unique = set()
            for a,b,c,d in sorted_el:
                unique.add((a,b))
            all_uniques.append(len(unique))
    return max(all_uniques)

def main():
    file_contents = ReadFile("Inputs.txt")
    answer = PartASolve(file_contents)
    print("Part A Answer: ", answer)
    answer = PartBSolve(file_contents)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
