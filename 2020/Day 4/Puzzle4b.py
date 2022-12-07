"""
Puzzle #4a - AdventOfCode
Read in a passport file and parse each passport into a new element of a list
Define required fields and check each entry for all required fields
Output total valid passports
"""
import math
import re

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

def ListToDict(Passports):
    PassportList = []
    for Passport in Passports:
        PassportDictionary = {}
        for Line in Passport.split("\n"):
            for KeyValuePair in Line.split(" "):
                Item = KeyValuePair.split(":")
                if Item[0] != "":
                    PassportDictionary[Item[0]] = Item[1]
        PassportList.append(PassportDictionary)

    return PassportList
        
        

def ValidatePassports(PassportList, RequiredFields):
    ValidPassports = 0
    HasRequiredFields = True
    for Passport in PassportList:       
        for RequiredField in RequiredFields:
            HasRequiredFields = True
            if RequiredField not in Passport:
                HasRequiredFields = False
                break
                
        if HasRequiredFields == False:
            continue

        else:
            Valid = True
            Valid = Valid and (len(Passport["byr"])==4) and (int(Passport["byr"])>=1920 and int(Passport["byr"])<=2002)
            Valid = Valid and (len(Passport["iyr"])==4) and (int(Passport["iyr"])>=2010 and int(Passport["iyr"])<=2020)
            Valid = Valid and (len(Passport["eyr"])==4) and (int(Passport["eyr"])>=2020 and int(Passport["eyr"])<=2030)
            HeightString = Passport["hgt"]
            if HeightString.find("cm") != -1:
               Valid = Valid and (int(HeightString[:-2]) >=150 and int(HeightString[:-2]) <=193)
            elif HeightString.find("in") != -1:
                Valid = Valid and (int(HeightString[:-2]) >=59 and int(HeightString[:-2]) <=76)
            else:
                Valid = False
            Valid = Valid and re.match(r"\#[0-9a-f]{6}", Passport["hcl"])
            Valid = Valid and Passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            Valid = Valid and (Passport["pid"].isdigit() and len(Passport["pid"]) == 9)

        if Valid == True:
            ValidPassports += 1
               
    return ValidPassports
                
        

def main():
    RequiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    Passports = ReadInFile()
    PassportList = ListToDict(Passports)
    NumberValidPassports = ValidatePassports(PassportList, RequiredFields)
    print("Number Of Valid Passports: ", NumberValidPassports)

if __name__ == "__main__":
    main()
