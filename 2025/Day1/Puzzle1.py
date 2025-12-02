def ReadInputs():
        File = open("./Inputs.txt", "r")

        Lines = [x.strip() for x in File]
        return Lines
    
def solveA(Input):
    size = 100
    counter = 50
    result = 0
    for line in Input:
        modifier = 0
        if line[0] == "L":
            modifier = -1
        else:
            modifier = 1
        amount = int(line[1:])
        amount = amount%size
        new_counter = counter + (modifier*amount)
        if new_counter >= size:
            new_counter = new_counter%size
        elif new_counter < 0:
            new_counter = size+new_counter

        counter = new_counter
        if counter == 0:
            result +=1
    return result

def solveB(Input):
    size = 100
    counter = 50
    result = 0
    for line in Input:
        modifier = 0
        if line[0] == "L":
            modifier = -1
        else:
            modifier = 1
        amount = int(line[1:])
        result += amount//size
        amount = amount%size
        new_counter = counter + (modifier*amount)

        if new_counter >= size:
            new_counter = new_counter%size
            result +=1
        elif new_counter < 0:
            new_counter = size+new_counter
            if counter != 0:
                result +=1
        elif new_counter == 0:
            result +=1

        counter = new_counter
    return result

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
