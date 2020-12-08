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
    BagTree = ["shiny gold"]
    RelevantRules = {}

    for DesiredBag in BagTree:
        for Rule in Rules:
            TempList = []
            if Rule.find(DesiredBag) != -1 and Rule.find(DesiredBag) == 0:
                Key = Rule.split("contain")[0][:-6]
                Values = Rule.split("contain")[1]

                if Values.startswith(" no"):
                    continue
                    
                Values = Values.split(", ")
                
                for Item in Values:
                    Items = Item.split()
                    Count = Items[0]
                    InnerBag = Items[1] + " " + Items[2]
                    if  InnerBag not in DesiredBag:
                        BagTree.append(InnerBag)
                    FullItem = Count + " " + InnerBag
                    TempList.append(FullItem)
                RelevantRules[Key] = TempList
      
    return RelevantRules

def Calculate(RelevantRules, DesiredBag):
    Answer = 1
    if DesiredBag in RelevantRules:
        for Values in RelevantRules[DesiredBag]:
            Count = int(Values[0])
            SubBag = Values[2:]
            Answer += Count * Calculate(RelevantRules, SubBag)
            print("DesiredBag: ", DesiredBag)
            print("NextBag: ", SubBag)
            print("Answer: ", Answer)
    else:
        Answer = 1

    return Answer
            
            
        
                
def main():
    Rules = ReadInFile()
    RelevantRules = ParseRules(Rules)
    DesiredBag = "shiny gold"
    Answer = Calculate(RelevantRules, DesiredBag)
    print("The number of bags inside the gold bag is: ", Answer-1)

if __name__ == "__main__":
    main()
