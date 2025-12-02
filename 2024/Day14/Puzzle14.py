from collections import deque

def ReadFile(filename):
    content = open(filename).read().strip()
    return content

    return content
            
def PartASolve(inputs,step):
    width = 101
    height = 103
    robots = []
    
    q1xmin = 0
    q1xmax = (width-1)//2
    q1ymin = 0
    q1ymax = (height-1)//2
    
    q2xmin = ((width-1)//2)+1
    q2xmax = width
    q2ymin = 0
    q2ymax = (height-1)//2
    
    q3xmin = 0
    q3xmax = (width-1)//2
    q3ymin = ((height-1)//2)+1
    q3ymax = height
    
    q4xmin = ((width-1)//2)+1
    q4xmax = width
    q4ymin = ((height-1)//2)+1
    q4ymax = height

    quadrants = [0,0,0,0]
    robots = inputs.split("\n")
    for robot in robots:
        px,py = robot.split()[0][2:].split(",")
        vx,vy = robot.split()[1][2:].split(",")
        dx = (int(vx)*step)%width
        dy = (int(vy)*step)%height
        npx = int(px)+dx
        npy = int(py)+dy

        if npx < 0:
            npx = width-npx
        elif npx >= width:
            npx = npx%width

        if npy < 0:
            npy = height-npy
        elif npy >= height:
            npy = npy%height

        if q1xmin <= npx < q1xmax and q1ymin <= npy < q1ymax:
            quadrants[0]+=1
        elif q2xmin <= npx < q2xmax and q2ymin <= npy < q2ymax:
            quadrants[1]+=1
        elif q3xmin <= npx < q3xmax and q3ymin <= npy < q3ymax:
            quadrants[2]+=1
        elif q4xmin <= npx < q4xmax and q4ymin <= npy < q4ymax:
            quadrants[3]+=1
    total = 1

    for q in quadrants:
        total *= q
    return total

def PartBSolve(inputs,step):
    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    width = 101
    height = 103
    robots = []

    data = inputs.split("\n")
    for robot in data:
        px,py = robot.split()[0][2:].split(",")
        vx,vy = robot.split()[1][2:].split(",")
        robots.append((int(px), int(py), int(vx), int(vy)))
            
    count = 1
    while True:
        Grid = [['.' for x in range(width)] for y in range(height)]
        for i,(px,py,vx,vy) in enumerate(robots):
            npx = px+vx
            npy = py+vy

            if npx < 0:
                npx = width+npx
            elif npx >= width:
                npx = npx%width

            if npy < 0:
                npy = height+npy
            elif npy >= height:
                npy = npy%height
            robots[i] = (npx,npy,vx,vy)
            Grid[npy][npx] = "#"
        
        Seen = set()
        components = 0
        for y in range(height):
            for  x in range(width):
                if Grid[y][x] == "#" and (x,y) not in Seen:
                    sx,sy = x,y
                    components += 1
                    Q = deque([(sx,sy)])
                    while Q:
                        x2,y2 = Q.popleft()
                        if (x2,y2) in Seen:
                            continue
                        Seen.add((x2,y2))
                        for dx,dy in DIRS:
                            xx,yy = x2+dx,y2+dy
                            if 0<=xx<width and 0<=yy<height and Grid[yy][xx]=='#':
                                Q.append((xx,yy))
        if components <= 200:
            return count

        count+=1        

        

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs,100)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs,100)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
