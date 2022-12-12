def ReadInputs():
        File = open("./Inputs.txt", "r")
        Trees = [Line.strip() for Line in File]

        return Trees  
  
def solveA(Trees):
    VisibleTrees = {}

    for RowIndex, Rows in enumerate(Trees):
        for ColumnIndex, Column in enumerate(Rows):

            StringIndex = str(ColumnIndex) + "," + str(RowIndex)

            if ColumnIndex == 0 or ColumnIndex == len(Rows)-1:
                VisibleTrees[StringIndex] = Column
                continue

            if RowIndex == 0 or RowIndex == len(Trees)-1:
                VisibleTrees[StringIndex] = Column
                continue
            Visible = True
            for i in range(ColumnIndex+1, len(Rows)):
                if int(Column) <= int(Rows[i]):
                    Visible = False

            if Visible == True:
                VisibleTrees[StringIndex] = Column
                Visible = False
                continue
            Visible = True
            for i in range(ColumnIndex):
                if int(Column) <= int(Rows[i]):
                    Visible = False

            if Visible == True:
                VisibleTrees[StringIndex] = Column
                Visible = False
                continue
            Visible = True       
            for i in range(RowIndex+1, len(Trees)):
                if int(Column) <= int(Trees[i][ColumnIndex]):
                    Visible = False

            if Visible == True:
                VisibleTrees[StringIndex] = Column
                Visible = False
                continue
            Visible = True
            for i in range(RowIndex):
                if int(Column) <= int(Trees[i][ColumnIndex]):
                    Visible = False

            if Visible == True:
                VisibleTrees[StringIndex] = Column
                Visible = False
                continue
    return len(VisibleTrees)

def solveB(Trees):
    ScenicScore = {}

    for RowIndex, Rows in enumerate(Trees):
        for ColumnIndex, Column in enumerate(Rows):

            StringIndex = str(ColumnIndex) + "," + str(RowIndex)

            if ColumnIndex == 0 or ColumnIndex == len(Rows)-1:
                continue

            if RowIndex == 0 or RowIndex == len(Trees)-1:
                continue

            TreeCounts = []

            TreeCount = 0
            # Looking Right
            for i in range(ColumnIndex+1, len(Rows)):
                if int(Column) > int(Rows[i]):
                    TreeCount +=1
                elif int(Column) <= int(Rows[i]):
                    TreeCount +=1
                    break
            TreeCounts.append(TreeCount)
                    
            TreeCount = 0
            # Looking Left
            for i in reversed(range(ColumnIndex)):
                if int(Column) > int(Rows[i]):
                    TreeCount +=1
                elif int(Column) <= int(Rows[i]):
                    TreeCount +=1
                    break
            TreeCounts.append(TreeCount)

            TreeCount = 0
            # Looking Down
            for i in range(RowIndex+1, len(Trees)):
                if int(Column) > int(Trees[i][ColumnIndex]):
                    TreeCount +=1
                elif int(Column) <= int(Trees[i][ColumnIndex]):
                    TreeCount +=1
                    break
            TreeCounts.append(TreeCount)

            TreeCount = 0
            # Looking Up
            for i in reversed(range(RowIndex)):
                if int(Column) > int(Trees[i][ColumnIndex]):
                    TreeCount +=1
                elif int(Column) <= int(Trees[i][ColumnIndex]):
                    TreeCount +=1
                    break
            TreeCounts.append(TreeCount)
            TreeCount = 0

            ScenicScore[StringIndex]=TreeCounts
            TreeCounts = []
    PossibleAnswers = []
    for Key, Value in ScenicScore.items():
        Result =1
        for Number in Value:
            Result*=Number
        PossibleAnswers.append(Result)

    return max(PossibleAnswers)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
