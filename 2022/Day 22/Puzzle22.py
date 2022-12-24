def ReadInputs():
        File = open("./Inputs.txt", "r")
        Directions = []
        Map = []
        Data = File.read().split("\n\n")

        MaxWidth = max([len(Line) for Line in Data[0].split("\n")])
        for Lines in Data[0].split("\n"):
            if len(Lines) != MaxWidth:
                Pad = MaxWidth - len(Lines)
                NewLine = Lines + " " * Pad
                Map.append(NewLine)
                continue
            Map.append(Lines)

        Direction = ""
        for Character in Data[1]:
            if Character.isdigit():
                Direction+=Character
            else:
                Directions.append(Direction)
                Directions.append(Character)
                Direction = ""
        Directions.append(Direction)

        return Map, Directions

    
def solveA(Map,Directions):
    MapWidth = len(Map[0])
    MapHeight = len(Map)   
    CurrentHeading = (0,1)
    Row = [Map[0][x] for x in range(MapWidth)]
    Row = "".join(x for x in Row)
    StartingColumn = Row.find(".")
    CurrentPosition = (0,StartingColumn)
    for Step in Directions:
        if Step.isdigit():
            print("CurrentPosition: ", CurrentPosition)
            row,col = CurrentPosition
            drow, dcol = CurrentHeading
            for i in range(1,int(Step)+1):
                new_col = col + (dcol)
                new_row = row + (drow)

                if new_col < 0 or new_col >= MapWidth:
                    #print("End of Row")
                    wrapped_col = new_col%MapWidth
                    if Map[new_row][wrapped_col] == "#":
                        CurrentPosition = (row,col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                        break
                    if Map[new_row][wrapped_col] == ".":
                        CurrentPosition = (new_row, wrapped_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                    else:
                        map_row = [Map[new_row][x] for x in range(MapWidth)]
                        map_row = "".join(x for x in map_row)
                        if wrapped_col == 0:
                            new_col = map_row.find(".")
                        else:
                            new_col = map_row.rfind(".")
                        CurrentPosition = (new_row, new_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)

                elif new_row < 0 or new_row >= MapHeight:
                    #print("End of Column")
                    wrapped_row = new_row%MapHeight
                    if Map[wrapped_row][new_col] == "#":
                        CurrentPosition = (row,col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                        break
                    if wrapped_row == ".":
                        CurrentPosition = (wrapped_row, new_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                    else:
                        map_col = [Map[x][new_col] for x in range(MapHeight)]
                        map_col = "".join(x for x in map_col)
                        if wrapped_row == 0:
                            new_row = map_col.find(".")
                        else:
                            new_row = map_col.rfind(".")
                        CurrentPosition = (new_row, new_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)

                elif Map[row+(drow)][col+(dcol)] == " ":
                    #print("End of Dots")
                    if dcol == 0:
                        map_col = [Map[x][new_col] for x in range(MapHeight)]
                        map_col = "".join(x for x in map_col)
                        if drow == 1:
                            new_row = map_col.find(".")
                        else:
                            new_row = map_col.rfind(".")
                        CurrentPosition = (new_row, new_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                    else:
                        map_row = [Map[new_row][x] for x in range(MapWidth)]
                        map_row = "".join(x for x in map_row)
                        if dcol == 1:
                            new_col = map_row.find(".")
                        else:
                            new_col = map_row.rfind(".")
                        CurrentPosition = (new_row, new_col)
                        #print("Current Position: ",CurrentPosition)
                        #print("Current Heading: ", CurrentHeading)
                elif Map[row+(drow)][col+(dcol)] == "#":
                    #print("Hit a wall")
                    CurrentPosition = (row, col)
                    #print("Current Position: ",CurrentPosition)
                    #print("Current Heading: ", CurrentHeading)
                    break
                else:
                    CurrentPosition = (new_row, new_col)
                    #print("Current Position: ",CurrentPosition)
                    #print("Current Heading: ", CurrentHeading)
        elif Step == "R":
            if CurrentHeading == (0,1):
                CurrentHeading = (1,0)
            elif CurrentHeading == (0,-1):
                CurrentHeading = (-1,0)
            elif CurrentHeading == (-1,0):
                CurrentHeading = (0,1)
            elif CurrentHeading == (1,0):
                CurrentHeading = (0,-1)
        else:
            if CurrentHeading == (0,1):
                CurrentHeading = (-1,0)
            elif CurrentHeading == (0,-1):
                CurrentHeading = (1,0)
            elif CurrentHeading == (-1,0):
                CurrentHeading = (0,-1)
            elif CurrentHeading == (1,0):
                CurrentHeading = (0,1)

    return CurrentPosition

def solveB(Map,Directions):
    return

def main():

    Map,Directions=ReadInputs()
    Part1=solveA(Map,Directions)
    print("Answer: ", Part1)
    Part2=solveB(Map,Directions)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
