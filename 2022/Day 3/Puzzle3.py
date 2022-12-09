import string
def ReadInputs():
    File = open("./Inputs.txt", "r")
    Rucksacks = []
    
    for Line in File:
    	Rucksacks.append(Line.strip())
 
    return Rucksacks
    
def solveA(Rucksacks):
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    alphabet = lower_alphabet + upper_alphabet

    score = {}
    value =1
    for letter in alphabet:
        score[letter] = value
        value += 1

    DuplicateItems = []
    for Rucksack in Rucksacks:
        CompartmentOne = Rucksack[:len(Rucksack)//2]
        CompartmentTwo = Rucksack[len(Rucksack)//2:]

        for Item1 in CompartmentOne:
            if Item1 in CompartmentTwo:
                DuplicateItems.append(Item1)
                break
        
    total = 0
    for Item in DuplicateItems:
        total += score[Item]

    return total
    
def solveB(Rucksacks): 
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase
    alphabet = lower_alphabet + upper_alphabet

    score = {}
    value =1
    for letter in alphabet:
        score[letter] = value
        value += 1
    
    groups = []
    group = []
    count = 0
    for Rucksack in Rucksacks:
        group.append(Rucksack)
        count += 1
        if count == 3:
            groups.append(group)
            group = [] 
            count = 0

    badges = []
    for group in groups:
        RucksackOne = group[0]
        RucksackTwo = group[1]
        RucksackThree = group[2]

        for Item in RucksackOne:
            if Item in RucksackTwo and Item in RucksackThree:
                badges.append(Item)
                break

    total = 0
    for badge in badges:
        total += score[badge]

    return total


    

    return
    
def main():

    Inputs=ReadInputs()
    Part1=solveA(Inputs)
    print("Answer: ", Part1)
    Part2=solveB(Inputs)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
