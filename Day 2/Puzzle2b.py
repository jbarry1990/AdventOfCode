"""
Puzzle #2b - AdventOfCode
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
    FirstIndex = int(Entry[0:DashIndex])-1
    SecondIndex = int(Entry[DashIndex+1:FirstSpaceIndex])-1
    ImportantCharacter = Entry[FirstSpaceIndex+1]
    StringToSearch = Entry[ColonIndex+2:]
        
    return FirstIndex, SecondIndex, ImportantCharacter, StringToSearch

def ValidateEntry(FirstIndex,
                  SecondIndex,
                  ImportantCharacter,
                  StringToSearch):

    IsFirstNotSecond = StringToSearch[FirstIndex] == ImportantCharacter and StringToSearch[SecondIndex] != ImportantCharacter
    IsSecondNotFirst = StringToSearch[FirstIndex] != ImportantCharacter and StringToSearch[SecondIndex] == ImportantCharacter
    if IsFirstNotSecond ^ IsSecondNotFirst:
        return True
    else:
        return False

def main():
    NumberOfValidPasswords = 0
    
    PasswordList = ReadInFile()

    for Entry in PasswordList:
        FirstIndex,SecondIndex,ImportantCharacter,StringToSearch = ParseEntry(Entry)
        
        IsValid = ValidateEntry(FirstIndex,
                                SecondIndex,
                                ImportantCharacter,
                                StringToSearch)

        if IsValid == True:
            NumberOfValidPasswords += 1

    print("The number of valid passwords is ", NumberOfValidPasswords)
        
    

if __name__ == "__main__":
    main()
