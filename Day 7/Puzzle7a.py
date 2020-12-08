"""
Puzzle #7a - AdventOfCode
Read in rules list
Parse rules to determine what bags can hold gold bags
Iteratively parse rules to see which bags can hold those bags and so on and so forth
Sum the total of bags that can directly or indirectly hold a gold bag
"""
import math

def ReadInFile():
    File = open("./Rules.txt", "r")
    Rules = []

    for Entry in File:
            Rules.append(Entry)

    return Rules

def WriteToFile(Output):
    File = open("./Output.txt", "w")
    for Line in Output:
        File.write(Line + "\n")
    return

def ParseRules(Rules):
    ContainsDesiredBag = ["shiny gold"]

    for DesiredBag in ContainsDesiredBag:
        for Rule in Rules:
            if Rule.find(DesiredBag) != -1:
                if Rule.find(DesiredBag) !=0:
                    Index = Rule.find("bags")
                    if Rule[0:Index-1] not in ContainsDesiredBag:
                        ContainsDesiredBag.append(Rule[0:Index-1])

    print(ContainsDesiredBag)
            
    return ContainsDesiredBag
            
            
        
                
def main():
    Rules = ReadInFile()
    ContainsDesiredBag = ParseRules(Rules)
    print("The number of bags that will allow you to eventually use a shiny gold bag is: ", len(ContainsDesiredBag)-1)
    WriteToFile(ContainsDesiredBag)

if __name__ == "__main__":
    main()
