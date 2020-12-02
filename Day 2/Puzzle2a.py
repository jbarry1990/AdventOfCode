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
        
    return ListOfEntries

def ParseEntry(Entry):
    return

def ValidateEntry(ParsedEntry):
    return

def main():
    PasswordList = ReadInFile()
    

if __name__ == "__main__":
    main()
