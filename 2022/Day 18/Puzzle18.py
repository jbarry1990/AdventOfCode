def ReadInputs():
        File = open("./Inputs.txt", "r")
        Coordinates = []

        for Line in File:
            Coordinate = Line.strip().split(",")
            Coordinate = [int(x) for x in Coordinate]
            Coordinates.append(Coordinate)

        return Coordinates
    
def solveA(Coordinates):
    OpenSides={"({},{},{})".format(Coordinate[0],Coordinate[1],Coordinate[2]) :6 for Coordinate in Coordinates}
    
    for Coordinate in Coordinates:
        Key = "({},{},{})".format(Coordinate[0],Coordinate[1],Coordinate[2])
        for OtherCoordinate in Coordinates:
            if OpenSides[Key]==0:
                break

            X1 = Coordinate[0]
            Y1 = Coordinate[1]
            Z1 = Coordinate[2]
            X2 = OtherCoordinate[0]
            Y2 = OtherCoordinate[1]
            Z2 = OtherCoordinate[2]

            if X1 == X2 and Y1 == Y2 and abs(Z1-Z2) == 1:
                OpenSides[Key] -=1
            elif X1 == X2 and Z1 == Z2 and abs(Y1-Y2)==1:
                OpenSides[Key] -=1
            elif Y1 == Y2 and Z1 == Z2 and abs(X1-X2)==1:
                OpenSides[Key] -=1

    Answer = 0
    for Key,Value in OpenSides.items():
        Answer += Value
    return Answer

def solveB(Input):
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
