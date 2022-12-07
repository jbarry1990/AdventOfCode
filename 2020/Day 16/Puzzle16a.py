"""
Puzzle #16a - AdventOfCode
1. Read from input file. Parse file into three sections, Rules, My Ticket, Nearby Tickets
2. Using Rules validate nearby tickets. If a value on a nearby ticket is invalid add that value to a list
3. Sum the invalid values and output the result
"""
from time import time

def ReadInFile():
    File = open("./PuzzleInput.txt", "r")
    Rules = {}
    MyTicket = []
    NearbyTickets = []
    Section1Done = False
    Section2Done = False

    for Entry in File:
        if Section1Done == False:
            if Entry == "\n":
                Section1Done = True
                continue
            
            Key = Entry.strip().split(":")[0]
            EntireValue = Entry.strip().split(":")[1].split(" or ")
            Value = []
            for SubValue in EntireValue:
                Result = SubValue.split("-")
                for Number in Result:
                    Value.append(int(Number))
            Rules[Key] = Value

        if Section2Done == False and Section1Done == True:
            if Entry == "\n":
                Section2Done = True
                continue

            if Entry.startswith("your"):
                continue
            MyTicket = Entry.strip().split(",")
    
        if Section1Done == True and Section2Done == True:
            if Entry.startswith("nearby"):
                continue

            NearbyTickets.append(Entry.strip().split(","))

    for NearbyTicket in NearbyTickets:
        for Index, Data in enumerate(NearbyTicket):
            NearbyTicket[Index] = int(Data)
  
    return Rules, MyTicket, NearbyTickets

def FindInvalidValues(Rules, NearbyTickets):
    InvalidValues = []

    for Ticket in NearbyTickets:
        for Data in Ticket:
            Valid = False
            for Rule in Rules:
                Ranges = Rules[Rule]
                Valid = ((Data>=Ranges[0] and Data<=Ranges[1]) or (Data >=Ranges[2] and Data<=Ranges[3]))
                if Valid == False:
                    continue
                else:
                    Valid = True
                    break
            if Valid == False:
                InvalidValues.append(Data)
        
    return InvalidValues

def SumInvalidNumbers(InvalidNumbers):
    return sum(InvalidNumbers)

def main():
    t_start = time()
    
    Rules, MyTicket, NearbyTickets = ReadInFile()
    InvalidValues = FindInvalidValues(Rules, NearbyTickets)
    Answer = SumInvalidNumbers(InvalidValues)
    
    print("Part 1: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
