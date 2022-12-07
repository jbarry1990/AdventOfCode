"""
Puzzle #16b - AdventOfCode
1. Read from input file. Parse file into three sections, Rules, My Ticket, Nearby Tickets
2. Using Rules validate nearby tickets. If a value on a nearby ticket is invalid remove that ticket
3. Using the valid tickets and the rules determine what order each field appears on the ticket
4. Look at your ticket for the six fields that start with depature and multiply those together
5.Output the result
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

def FindValidTickets(Rules, NearbyTickets):
    ValidTickets = []

    for Ticket in NearbyTickets:
        TicketValid = True
        for Data in Ticket:
            DataValid = False
            for Rule in Rules:
                Ranges = Rules[Rule]
                DataValid = ((Data>=Ranges[0] and Data<=Ranges[1]) or (Data >=Ranges[2] and Data<=Ranges[3]))
                if DataValid == False:
                    continue
                else:
                    DataValid = True
                    break
            if DataValid == False:
                TicketValid = False
                break;
        if TicketValid == True:
            ValidTickets.append(Ticket)
        else:
            TicketValid = True
        
    return ValidTickets

def GroupInCorrespondingFields(ValidTickets):
    CorrespondingFields = []
    NumberOfFields = len(ValidTickets[0])
    
    for Length in range(NumberOfFields):
        FieldPosition = []
        for Ticket in ValidTickets:
            for Position, Field in enumerate(Ticket):
                if Position == Length:
                    FieldPosition.append(int(Field))    
        CorrespondingFields.append(FieldPosition)
                               
    return CorrespondingFields

def DetermineOrder(CorrespondingFields, Rules, PositionsOut):
    Positions = PositionsOut

    for Index, Fields in enumerate(CorrespondingFields, 1):
        SuccessfulRules = []
        for Rule in Rules:
            Ranges = Rules[Rule]
            DataValid = False
            for Data in Fields:
                DataValid = ((Data>=Ranges[0] and Data<=Ranges[1]) or (Data >=Ranges[2] and Data<=Ranges[3]))
                if DataValid == False:
                    break
            if DataValid == True:
                SuccessfulRules.append(Rule)
        if len(SuccessfulRules) == 1:
            Positions[Index] = SuccessfulRules[0]
            del Rules[SuccessfulRules[0]]

    if len(Rules) > 1:
        DetermineOrder(CorrespondingFields, Rules, Positions)

    else:
        return
    
    return Positions

def FindDepartureAndMultiply(Positions, MyTicket):
    Results=[]
    Answer = 1
    
    for Position in Positions:
        if Positions[Position].startswith("departure"):
            Results.append(Position)

    for Index,Positions in enumerate(MyTicket,1):
        if Index in Results:
            Answer *= int(Positions)
    return Answer

def main():
    t_start = time()
    
    Rules, MyTicket, NearbyTickets = ReadInFile()
    ValidTickets = FindValidTickets(Rules, NearbyTickets)
    CorrespondingFields = GroupInCorrespondingFields(ValidTickets)
    Positions = DetermineOrder(CorrespondingFields, Rules, PositionsOut = {})
    Answer = FindDepartureAndMultiply(Positions, MyTicket)
    
    print("Part 2: ", Answer)
    
    elapsed = 1000 * (time() - t_start)
    print("Time: %.3fms" % elapsed)
    
if __name__ == "__main__":
    main()
