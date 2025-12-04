def ReadInputs():
    File = open("./Inputs.txt", "r")
    results = [line.strip() for line in File]
    return results
    
def solveA(Input):
    results = []
    for bank in Input:
        nums = ""
        for i in range(9,0,-1):
            index1 = bank.find(str(i))
            if index1 == -1 or index1 == len(bank)-1:
                continue
            nums += bank[index1]
            break

            
        new_bank = bank[index1+1:]
        for i in range(9,0,-1):
            index2 = new_bank.find(str(i))
            if index2 != -1:
                nums += new_bank[index2]
                break
        results.append(int(nums))
    return sum(results)

def solveB(Input):
    results = []
    for bank in Input:
        nums = ""
        start = 0
        new_bank = bank[start:]
        while len(nums)<12:
            new_bank = new_bank[start:]
            for i in range(9,0,-1):
                index = new_bank.find(str(i))
                if index != -1 and len(new_bank)-1 - index >= 12-len(nums)-1:
                    nums += new_bank[index]
                    start = index+1
                    break
        
        results.append(int(nums))        
    return sum(results)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
