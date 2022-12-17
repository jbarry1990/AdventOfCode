import string
def ReadInputs():
        File = open("./Inputs.txt", "r")

        Map = [Line.strip() for Line in File]

        return Map
    
def solveA(Map):

    ShortestPathLength = 0
    RowLength = len(Map)
    ColumnLength = len(Map[0])

    Queue = []
    Visited = set()
    Elevation ={}

    for r in range(RowLength):
        if Queue != []:
            break
        for c in range(ColumnLength):
            if Map[r][c] == "S":
                Queue.append(((r,c), 0))
                break

    
    alphabet = string.ascii_lowercase
    for Index, Letter in enumerate(alphabet):
        Elevation[Letter] = Index + 1
    Elevation["S"] = 1
    Elevation["E"] = 26

    FoundDestination = False
    while Queue or FoundDestination == False:
        (Row, Column), Depth = Queue.pop()
        if (Row, Column) in Visited:
            continue
        Visited.add((Row, Column))

        if Map[Row][Column] == "E":
            ShortestPathLength = Depth
            FoundDestination = True
            continue

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            NewRow = Row+dr
            NewColumn = Column+dc
            if 0 <= NewRow < RowLength and 0 <= NewColumn < ColumnLength and Elevation[Map[NewRow][NewColumn]] <= Elevation[Map[Row][Column]]+1:
                Queue.insert(0,((NewRow,NewColumn), Depth+1))

    return ShortestPathLength

def solveB(Map):
    ShortestPathLength = 0
    RowLength = len(Map)
    ColumnLength = len(Map[0])

    Queue = []
    Visited = set()
    Elevation ={}

    for r in range(RowLength):
        for c in range(ColumnLength):
            if Map[r][c] == "S" or Map[r][c] == "a":
                Queue.append(((r,c), 0))

    
    alphabet = string.ascii_lowercase
    for Index, Letter in enumerate(alphabet):
        Elevation[Letter] = Index + 1
    Elevation["S"] = 1
    Elevation["E"] = 26

    FoundDestination = False
    while Queue or FoundDestination == False:
        (Row, Column), Depth = Queue.pop()
        if (Row, Column) in Visited:
            continue
        Visited.add((Row, Column))

        if Map[Row][Column] == "E":
            ShortestPathLength = Depth
            FoundDestination = True
            continue

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            NewRow = Row+dr
            NewColumn = Column+dc
            if 0 <= NewRow < RowLength and 0 <= NewColumn < ColumnLength and Elevation[Map[NewRow][NewColumn]] <= Elevation[Map[Row][Column]]+1:
                Queue.insert(0,((NewRow,NewColumn), Depth+1))

    return ShortestPathLength

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
