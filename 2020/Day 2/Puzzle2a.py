"""
Puzzle #2a - AdventOfCode
Read in a list of passwords
Parse the string for the rule and the associated password
Determine whether the password meets the rule
Increment a counter of valid passwords
"""

def ReadInFile():
    File = open("./PasswordList.txt", "r")
    ListOfEntries = []
    
    for Entries in File:
        ListOfEntries.append(Entries)

    print("NumberOfEntries:",len(ListOfEntries))
    return ListOfEntries

def ParseEntry(Entry):
    DashIndex = Entry.find("-")
    FirstSpaceIndex = Entry.find(" ")
    ColonIndex = Entry.find(":")
    LowerLimit = Entry[0:DashIndex]
    UpperLimit = Entry[DashIndex+1:FirstSpaceIndex]
    ImportantCharacter = Entry[FirstSpaceIndex+1]
    StringToSearch = Entry[ColonIndex+2:]
        
    return LowerLimit, UpperLimit, ImportantCharacter, StringToSearch

def ValidateEntry(LowerLimit,
                  UpperLimit,
                  ImportantCharacter,
                  StringToSearch):
    CharacterCounter = 0
    for Characters in StringToSearch:
        if Characters == ImportantCharacter:
            CharacterCounter +=1
    if CharacterCounter < int(LowerLimit) or CharacterCounter > int(UpperLimit):
        return False
    else:
        return True

def main():
    NumberOfValidPasswords = 0
    
    PasswordList = ReadInFile()

    for Entry in PasswordList:
        LowerLimit,UpperLimit,ImportantCharacter,StringToSearch = ParseEntry(Entry)
        
        IsValid = ValidateEntry(LowerLimit,
                                UpperLimit,
                                ImportantCharacter,
                                StringToSearch)

        if IsValid == True:
            NumberOfValidPasswords += 1

    print("The number of valid passwords is ", NumberOfValidPasswords)
        
    

if __name__ == "__main__":
    main()
