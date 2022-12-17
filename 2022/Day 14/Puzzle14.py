def ReadInputs():
        File = open("./Inputs.txt", "r")
        Data = File.read().strip()
        Rocks = []
        Rock = []
        for Line in Data.split("\n"):
            for Coordinate in Line.split(" -> "):
                x,y = Coordinate.split(",")
                Rock.append((int(x),int(y)))

            Rocks.append(Rock)
            Rock = []

        return Rocks

def BuildMap(Rocks):
    Map = [[]]
    LowerX = 1000
    UpperX = 0
    LowerY = 0

    for Rock in Rocks:
        for (x,y) in Rock:
            if x > UpperX:
                UpperX = x
            elif x < LowerX:
                LowerX = x
            if y > LowerY:
                LowerY = y

    Map = [["."  for Row in range(1000)] for Column in range(LowerY+1)]

    for Rock in Rocks:
        for Index, (x,y) in enumerate(Rock):
            if Index == len(Rock)-1:
                break
            (dx, dy) = Rock[Index+1]

            if x == dx:
                for yy in range(abs(y-dy)+1):
                    if y < dy:
                        Map[y+yy][x] = "#"
                    else:
                        Map[dy+yy][x] = "#"
            else:
                for xx in range(abs(x-dx)+1):
                    if x < dx:
                        Map[y][x+xx] = "#"
                    else:
                        Map[y][dx+xx] = "#"

    return Map, LowerX, UpperX, LowerY

def solveA(Rocks):
    Map, LowerX, UpperX, LowerY = BuildMap(Rocks)

    CurrentColumn = 500
    CurrentRow = 0
    GrainsOfSand = 0
    End = True
    while End:

        if CurrentRow + 1 >= len(Map) or CurrentColumn-1 < 0 or CurrentColumn+1 >= len(Map[0]):
            End = False
            continue

        if Map[CurrentRow+1][CurrentColumn] == ".":
            CurrentRow +=1
        elif Map[CurrentRow +1][CurrentColumn-1] == ".":
            CurrentRow +=1
            CurrentColumn -=1
        elif Map[CurrentRow +1][CurrentColumn+1] == ".":
            CurrentRow +=1
            CurrentColumn +=1
        else:
            Map[CurrentRow][CurrentColumn] = "o"
            GrainsOfSand +=1
            CurrentColumn = 500
            CurrentRow = 0
    return GrainsOfSand

def solveB(Rocks):
    Map, LowerX, UpperX, LowerY = BuildMap(Rocks)

    Map.append(["." for _ in range(1000)])
    Map.append(["#" for _ in range(1000)])

    CurrentColumn = 500
    CurrentRow = 0
    GrainsOfSand = 0
    End = True

    while End:

        if Map[0][500] == "o":
            End = False
            continue

        if Map[CurrentRow+1][CurrentColumn] == ".":
            CurrentRow +=1
        elif Map[CurrentRow +1][CurrentColumn-1] == ".":
            CurrentRow +=1
            CurrentColumn -=1
        elif Map[CurrentRow +1][CurrentColumn+1] == ".":
            CurrentRow +=1
            CurrentColumn +=1
        else:
            Map[CurrentRow][CurrentColumn] = "o"
            GrainsOfSand +=1
            CurrentColumn = 500
            CurrentRow = 0
    return GrainsOfSand

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
