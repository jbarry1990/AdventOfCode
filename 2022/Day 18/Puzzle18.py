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

def IsOutside(xIn,yIn,zIn,Coordinates):
    Seen = set()
    Queue = []
    Queue.append([xIn,yIn,zIn])
    while Queue != []:
        [x,y,z] = Queue.pop()

        if [x,y,z] in Coordinates:
            continue
        
        if x > max(maxX[0] for maxX in Coordinates):
            return True
        if x < min(minX[0] for minX in Coordinates):
            return True
        if y > max(maxY[1] for maxY in Coordinates):
            return True
        if y < min(minY[1] for minY in Coordinates):
            return True
        if z > max(maxZ[2] for maxZ in Coordinates):
            return True
        if z < min(minZ[2] for minZ in Coordinates):
            return True
        if (x+1,y,z) not in Seen:
            Queue.insert(0,[x+1,y,z])
            Seen.add((x+1,y,z))
        if (x-1,y,z) not in Seen:
            Queue.insert(0,[x-1,y,z])
            Seen.add((x-1,y,z))
        if (x,y+1,z) not in Seen:
            Queue.insert(0,[x,y+1,z])
            Seen.add((x,y+1,z))
        if (x,y-1,z) not in Seen:
            Queue.insert(0,[x,y-1,z])
            Seen.add((x,y-1,z))
        if (x,y,z+1) not in Seen:
            Queue.insert(0,[x,y,z+1])
            Seen.add((x,y,z+1))
        if (x,y,z-1) not in Seen:
            Queue.insert(0,[x,y,z-1])
            Seen.add((x,y,z-1))
    return False

def solveB(Coordinates):
    Answer = 0
    MaxX = max(x[0] for x in Coordinates)
    MaxY = max(y[1] for y in Coordinates)
    MaxZ = max(z[2] for z in Coordinates)
    MinX = min(x[0] for x in Coordinates)
    MinY = min(y[1] for y in Coordinates)
    MinZ = min(z[2] for z in Coordinates)
    for x,y,z in Coordinates:
        if IsOutside(x+1,y,z,Coordinates):
            Answer +=1
        if IsOutside(x-1,y,z,Coordinates):
            Answer +=1
        if IsOutside(x,y+1,z,Coordinates):
            Answer +=1
        if IsOutside(x,y-1,z,Coordinates):
            Answer +=1
        if IsOutside(x,y,z+1,Coordinates):
            Answer +=1
        if IsOutside(x+1,y,z-1,Coordinates):
            Answer +=1
        print(Answer)
    return Answer

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
