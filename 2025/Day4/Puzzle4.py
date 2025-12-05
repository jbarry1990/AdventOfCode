def ReadInputs():
    File = open("./Inputs.txt", "r")
    rolls = [line.strip() for line in File]
    return rolls
    
def solveA(Input):
    results = 0
    locations = set()
    for x,row in enumerate(Input):
        for y,col in enumerate(row):
            if col == "@":
                locations.add((x,y))
    dirs = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]

    for (x,y) in locations:
        count = 0
        for (dx,dy) in dirs:
            if (x+dx,y+dy) in locations:
                count += 1
        if count < 4:
            results +=1
            
    return results

def solveB(Input):
    results = 0
    locations = set()
    for x,row in enumerate(Input):
        for y,col in enumerate(row):
            if col == "@":
                locations.add((x,y))
    dirs = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]
    original_size = len(locations)
    old_size = len(locations)

    while True:
        remove = set()
        for (x,y) in locations:
            count = 0
            for (dx,dy) in dirs:
                if (x+dx,y+dy) in locations:
                    count += 1
            if count < 4:
                remove.add((x,y))
        locations -= remove
        if old_size == len(locations):
            break
        else:
            old_size = len(locations)

        new_size = len(locations)
            
    return original_size - len(locations)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
