def ReadInputs():
        File = open("./Inputs.txt", "r")

        Steps = [Line.strip().split() for Line in File]

        for Index, Step in enumerate(Steps):
            if len(Step) == 2:
                Step[1] = int(Step[1])

        return Steps
    
def solveA(Steps):
    Counter = 1
    Register = 1
    Tracker = {}
    for Step in Steps:
        if Step[0] == "noop":
            for i in range(1):
                Tracker[Counter] = Register
                Counter +=1
        elif Step[0] == "addx":
            for i in range(2):
                Tracker[Counter] = Register
                Counter +=1
            Register += Step[1]

    Total = Tracker[20]*20 + Tracker[60]*60 + Tracker[100]*100 + Tracker[140]*140 + Tracker[180]*180 + Tracker[220]*220
    return Total, Tracker

def solveB(Tracker):
    CRT = []
    for j in range(6):
        for i in range(40):
            Register = Tracker[(i+j*40)+1]
            Sprite = [Register-1, Register, Register +1]

            if i in Sprite:
                CRT.append("#")
            else:
                CRT.append(".")

    return CRT

def main():

    Input=ReadInputs()
    Part1,Tracker=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Tracker)
    Row = 0
    for j in range(6):
        print("".join(Part2[Row:Row+40]))
        Row = Row+40




   
if __name__ == "__main__":
    main()
