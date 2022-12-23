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
    CurrentHeading = (0,1)
    CurrentPosition = (0,0)
    MapWidth = len(Map[0])
    MapHeight = len(Map)
    for Step in Directions:
        if Step.isdigit():
            col,row = CurrentPosition
            dcol, drow = CurrentHeading
            for i in range(1,int(Step)+1):
                new_col = col + (dcol*i)
                new_row = row + (drow*i)
                if new_col < 0 or new_col > MapWidth or new_row < 0 or new_row > MapHeight:
                    Backwards = tuple(-x for x in CurrentHeading)
                    pass
#Need to continue developing code to wrap around the map






                elif Map[col+(dcol*i)][row+(drow*i)] == " ":
                    pass
                elif Map[col+(dcol*i)][row+(drow*i)] == "#":
                    CurrentPosition = (col+(dcol*(i-1)), row+(drow*(i-1)))
                    break
                elif Map[col+(dcol*i)][row+(drow*i)] == " ":
                    pass
                else:
                    CurrentPosition = (col+(dcol*i), row+(drow*i))
                #print(CurrentPosition)


                



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

    return

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
