from collections import deque

def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.read().strip()
    return content
            
def PartASolve(inputs):
    grid,directions = inputs.split("\n\n")
    directions = directions.split("\n")
    directions = "".join(directions)
    grid = [[x for x in y] for y in grid.split("\n")]
    dirs = {"^":(-1,0), ">":(0,1), "<":(0,-1), "v":(1,0)}
    size = len(grid)
    walls = []
    boxes = []
    location = None

    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "#":
                walls.append((x,y))

            elif col == "O":
                boxes.append((x,y))
            elif col == "@":
                location = (x,y)

    for d in directions:
        affected = []
        x,y = location
        dx,dy = dirs[d]
        cx = x
        cy = y
        while True:
            cx +=dx
            cy +=dy

            if (cx,cy) not in boxes and (cx,cy) not in walls:
                location = (x+dx,y+dy)
                for x2,y2 in reversed(affected):
                    boxes[boxes.index((x2,y2))] = (x2+dx,y2+dy)
                break
            elif (cx,cy) in boxes:
                affected.append((cx,cy))
            elif (cx,cy) in walls:
                break
            
    total = 0
    for x,y in boxes:
        total += (100*x+y)
    return total
def PartBSolve(inputs):
    grid,directions = inputs.split("\n\n")
    new_grid = ""
    for char in grid:
        if char == "\n":
            new_grid +=char
        if char == "#":
            new_grid+="##"
        if char == "O":
            new_grid+="[]"
        if char == ".":
            new_grid +=".."
        if char == "@":
            new_grid +="@."
    
    directions = directions.split("\n")
    directions = "".join(directions)
    grid = [[x for x in y] for y in new_grid.split("\n")]
    dirs = {"^":(-1,0), ">":(0,1), "<":(0,-1), "v":(1,0)}
    size = len(grid)
    walls = []
    boxes = []
    location = None

    for x,row in enumerate(grid):
        for y,col in enumerate(row):
            if col == "#":
                walls.append((x,y))

            elif col == "[":
                boxes.append([(x,y),(x,y+1)])
            elif col == "@":
                location = (x,y)

    for d in directions:
        affected = set()
        x,y = location
        dx,dy = dirs[d]
        cx = x
        cy = y
        Q = deque()
        Q.append((x,y))
        go = True
        visited = set()
        while Q:
            cx,cy = Q.popleft()
            cx +=dx
            cy +=dy

            if all((cx,cy) not in box for box in boxes) and (cx,cy) not in walls:
                continue
            elif (cx,cy) in walls:
                go = False
                break
            else:
                for i,box in enumerate(boxes):
                    if (cx,cy) in box:
                        affected.add(i)
                        if box[0] not in visited:
                            Q.append(box[0])
                            visited.add(box[0])
                        if box[1] not in visited:
                            Q.append(box[1])
                            visited.add(box[1])
                        break

        
        if go:
            location = (x+dx,y+dy)
            for index in affected:
                x1,y1 = boxes[index][0]
                x2,y2 = boxes[index][1]
                boxes[index] = [(x1+dx,y1+dy),(x2+dx,y2+dy)]
        
    total = 0
    for box in boxes:
        x,y = box[0]
        total += (100*x+y)
    return total       

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
