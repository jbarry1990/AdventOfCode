def ReadInputs():
    File = open("./Inputs.txt", "r")
    ranges = []
    for line in File:
        ranges = line.split(",")
    return ranges
    
def solveA(Input):
    result = []
    for interval in Input:
        x,y = interval.split("-")
        x = x.strip()
        y = y.strip()

        if len(x)%2 != 0 and len(y)%2 != 0:
            continue

        for a in range(int(x), int(y)+1):
            if len(str(a))%2 != 0:
                continue
            a = str(a)
            if a.count(a[:int(len(a)/2)]) == 2:
                result.append(int(a))
    return sum(result)

def solveB(Input):
    result = []
    for interval in Input:
        x,y = interval.split("-")
        x = x.strip()
        y = y.strip()

        for num in range(int(x), int(y)+1):
            for digit in range(0, len(str(num))):
                sub = str(num)[:digit+1]
                if len(str(num))%len(sub) != 0:
                    continue
                if str(num).count(sub) == len(str(num))/len(sub) and str(num).count(sub) > 1:
                    result.append(num)
                    break
                               
    return sum(result)

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
