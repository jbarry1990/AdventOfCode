"""
Puzzle #4a - AdventOfCode
Read in a passport file and parse each passport into a new element of a list
Define required fields and check each entry for all required fields
Output total valid passports
"""
import math

def ReadInFile():
    File = open("./PassportList.txt", "r")
    Passports = []

    Buffer = ""
    for Entry in File:
        if Entry =="\n":
            Passports.append(Buffer)
            Buffer = ""
        else:
            Buffer += Entry
    Passports.append(Buffer)

    return Passports

def ValidatePassports(Passports, RequiredFields):
    ValidPassports = 0
    IsValidPassport = True
    for Passport in Passports:
        for RequiredField in RequiredFields:
            if Passport.find(RequiredField) == -1:
                IsValidPassport = False
        if IsValidPassport == True:
            ValidPassports += 1

        else:
            IsValidPassport = True
    return ValidPassports
                
        

def main():
    RequiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    Passports = ReadInFile()
    NumberValidPassports = ValidatePassports(Passports, RequiredFields)
    print("Number Of Valid Passports: ", NumberValidPassports)

if __name__ == "__main__":
    main()
