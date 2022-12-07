"""
Puzzle #1a - AdventOfCode
Read in a list of numbers
Determine which two numbers in that list add up to 2020
Multiply those two numbers and ouput the result
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
            if FirstTerm != SecondTerm:
                Result = int(FirstTerm) + int(SecondTerm)
                if Result == 2020:
                    Equals2020 = True
                    CorrectTerms.append(FirstTerm)
                    CorrectTerms.append(SecondTerm)
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
