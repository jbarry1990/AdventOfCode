from collections import defaultdict

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def PartASolve(inputs):
    antinodes = set()
    antennas = defaultdict(list)
    xmin = 0
    ymin = 0
    xmax = len(inputs)
    ymax = len(inputs[0])-1
            
    for x,row in enumerate(inputs):
        for y,col in enumerate(row.strip()):
            if col != ".":
                antennas[col].append((x,y))

    for locations in antennas.values():
        for i,loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:
                x0,y0 = loc1
                x1,y1 = loc2
                rise = x1-x0
                run = y1-y0
                if rise != 0:
                    slope = rise/run
                else:
                    slope = None
                if slope > 0:
                    if y0 < y1:
                        lx = x0-abs(rise)
                        ly = y0-abs(run)
                        rx = x1+abs(rise)
                        ry = y1+abs(run)
                    else:
                        lx = x1-abs(rise)
                        ly = y1-abs(run)
                        rx = x0+abs(rise)
                        ry = y0+abs(run)
                        
                elif slope < 0:
                    if y0 < y1:
                        lx = x0+abs(rise)
                        ly = y0-abs(run)
                        rx = x1-abs(rise)
                        ry = y1+abs(run)
                    else:
                        lx = x1+abs(rise)
                        ly = y1-abs(run)
                        rx = x0-abs(rise)
                        ry = y0+abs(run)

                if xmin <= lx < xmax and ymin <= ly < ymax:
                    antinodes.add((lx,ly))
                if xmin <= rx < xmax and ymin <= ry < ymax:
                    antinodes.add((rx,ry))
                    
    return len(antinodes)
    

def PartBSolve(inputs):
    antinodes = set()
    antennas = defaultdict(list)
    xmin = 0
    ymin = 0
    xmax = len(inputs)
    ymax = len(inputs[0])-1
            
    for x,row in enumerate(inputs):
        for y,col in enumerate(row.strip()):
            if col != ".":
                antennas[col].append((x,y))

    for locations in antennas.values():
        for i,loc1 in enumerate(locations):
            for loc2 in locations[i+1:]:
                x0,y0 = loc1
                x1,y1 = loc2
                antinodes.add((x0,y0))
                antinodes.add((x1,y1))
                rise = x1-x0
                run = y1-y0
                if rise != 0:
                    slope = rise/run
                else:
                    slope = None

                if slope > 0:
                    if y0 < y1:
                        nums = min((y0-ymin)//abs(run),(x0-xmin)//abs(rise))
                        for i in range(nums):
                            lx = x0-(abs(rise)*(i+1))
                            ly = y0-(abs(run)*(i+1))
                            if xmin <= lx < xmax and ymin <= ly < ymax:
                                antinodes.add((lx,ly))
                                
                        nums = min((ymax-y1)//abs(run),(xmax-x1)//abs(rise))
                        for i in range(nums):
                            rx = x1+(abs(rise)*(i+1))
                            ry = y1+(abs(run)*(i+1))
                            if xmin <= rx < xmax and ymin <= ry < ymax:
                                antinodes.add((rx,ry))
                    else:
                        nums = min((y1-ymin)//abs(run),(x1-xmin)//abs(rise))
                        for i in range(nums):
                            lx = x1-(abs(rise)*(i+1))
                            ly = y1-(abs(run)*(i+1))
                            if xmin <= lx < xmax and ymin <= ly < ymax:
                                antinodes.add((lx,ly))
                                
                        nums = min((ymax-y0)//abs(run),(xmax-x0)//abs(rise))
                        for i in range(nums):
                            rx = x0+(abs(rise)*(i+1))
                            ry = y0+(abs(run)*(i+1))
                            print("rx,ry: ", rx,ry)
                            if xmin <= rx < xmax and ymin <= ry < ymax:
                                antinodes.add((rx,ry))
                        
                elif slope < 0:
                    if y0 < y1:
                        nums = min((y0-ymin)//abs(run),(xmax-x0)//abs(rise))
                        for i in range(nums):
                            lx = x0+(abs(rise)*(i+1))
                            ly = y0-(abs(run)*(i+1))
                            if xmin <= lx < xmax and ymin <= ly < ymax:
                                antinodes.add((lx,ly))
                                
                        nums = min((ymax-y1)//abs(run),(x1-xmin)//abs(rise))
                        for i in range(nums):  
                            rx = x1-(abs(rise)*(i+1))
                            ry = y1+(abs(run)*(i+1))
                            if xmin <= rx < xmax and ymin <= ry < ymax:
                                antinodes.add((rx,ry))
                    else:
                        nums = min((y1-ymin)//abs(run),(xmax-x1)//abs(rise))
                        for i in range(nums):
                            lx = x1+(abs(rise)*(i+1))
                            ly = y1-(abs(run)*(i+1))
                            if xmin <= lx < xmax and ymin <= ly < ymax:
                                antinodes.add((lx,ly))
                                
                        nums = min((ymax-y0)//abs(run),(x0-xmin)//abs(rise))
                        for i in range(nums): 
                            rx = x0-(abs(rise)*(i+1))
                            ry = y0+(abs(run)*(i+1))
                            if xmin <= rx < xmax and ymin <= ry < ymax:
                                antinodes.add((rx,ry))
                    
    return len(antinodes)

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
