"""
Puzzle #1b - AdventOfCode
Read in a list of numbers
Determine which three numbers in that list add up to 2020
Multiply those three numbers and ouput the result
"""

def ReadInExpenseReport():
    File = open("./ExpenseReport.txt", "r")
    ExpenseEntries = []
    
    for Entries in File:
        ExpenseEntries.append(Entries)
        
    return ExpenseEntries

def FindEntriesThatAddTo2020(ExpenseList):
    Equals2020 = False
    CorrectTerms = []
    
    for FirstTerm in ExpenseList:
        if Equals2020 == True:
            break
        for SecondTerm in ExpenseList:
            if Equals2020 ==True:
                break
            for ThirdTerm in ExpenseList:
                if (FirstTerm != SecondTerm) and (SecondTerm !=ThirdTerm):
                    Result = int(FirstTerm) + int(SecondTerm) + int(ThirdTerm)
                    if Result == 2020:
                        Equals2020 = True
                        CorrectTerms.append(FirstTerm)
                        CorrectTerms.append(SecondTerm)
                        CorrectTerms.append(ThirdTerm)
                        break
    return CorrectTerms

def MultiplyResults(CorrectTerms):
    Result = 1
    for Terms in CorrectTerms:
        Result = Result * int(Terms)
    return Result

def main():
    ExpenseEntries = ReadInExpenseReport()
    CorrectTerms   = FindEntriesThatAddTo2020(ExpenseEntries)
    FinalResult    = MultiplyResults(CorrectTerms)
    for x in CorrectTerms:
        print("Term: ", x)
    print("The Final Result is ", FinalResult)

    

if __name__ == "__main__":
    main()
