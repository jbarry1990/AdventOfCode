def ReadInputs():
        File = open("./Inputs.txt", "r")

        Extents = []
        for Line in File.readlines():
            Line = Line.strip().split(":")
            LHS_X = int(Line[0].split()[2].split("=")[1][:-1])
            LHS_Y = int(Line[0].split()[3].split("=")[1])
            RHS_X = int(Line[1].split()[4].split("=")[1][:-1])
            RHS_Y = int(Line[1].split()[5].split("=")[1])
            Distance = abs(LHS_X - RHS_X) + abs(LHS_Y - RHS_Y)
            Top = LHS_Y - Distance
            Bottom = LHS_Y + Distance
            Left = LHS_X - Distance
            Right = LHS_X + Distance
            Extents.append([Top, Bottom, Left, Right])

        return Extents
    
def solveA(Extents, Line):
    Ranges = []
    for Sensor in Extents:
        Top = Sensor[0]
        Bottom = Sensor[1]
        Left = Sensor[2]
        Right = Sensor[3]
        X = abs(Left+Right)//2
        
        if Line >= Top and Line <= Bottom:
            Y = abs(Top+Bottom)//2
            Delta = abs(Line-Y)
            Ranges.append([Left+Delta, Right-Delta])

    Low = min([Range[0] for Range in Ranges])
    High = max([Range[1] for Range in Ranges])

    return High-Low

def solveB(Extents, Lines):
    YValue = -1
    FinalRange = []
    Count = 0
    for Line in range(Lines):
        Ranges = []
        for Sensor in Extents:
            Top = Sensor[0]
            Bottom = Sensor[1]
            Left = Sensor[2]
            Right = Sensor[3]
            
            if Line >= Top and Line <= Bottom:
                Y = abs(Top+Bottom)//2
                Delta = abs(Line-Y)
                Ranges.append([Left+Delta, Right-Delta])


        IndexL = 0
        IndexR = 0
        while IndexL < len(Ranges):
            while IndexR < len(Ranges):
                if IndexL != IndexR:
                    LeftX = Ranges[IndexL][0]
                    LeftY = Ranges[IndexL][1]
                    RightX = Ranges[IndexR][0]
                    RightY = Ranges[IndexR][1]
                    if (LeftY >= RightX) and (RightY >= LeftX):
                        merged = [min(LeftX, RightX), max(LeftY, RightY)]
                        del Ranges[max(IndexL, IndexR)]
                        del Ranges[min(IndexL, IndexR)]
                        Ranges.append(merged)
                        IndexL =0
                        IndexR = -1
                IndexR += 1
            IndexL +=1

        if len(Ranges)==2:
            YValue = Line
            FinalRange.append(Ranges)
            break

    
    return 3172756*4000000+YValue

def main():

    Input=ReadInputs()
    Part1=solveA(Input, 2000000)
    print("Answer: ", Part1)
    Input=ReadInputs()
    Part2=solveB(Input, 4000000)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
