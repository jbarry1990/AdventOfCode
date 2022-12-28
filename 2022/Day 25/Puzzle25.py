def ReadInputs():
    File = open("./Inputs.txt", "r")
    Numbers = [list(Line.strip()) for Line in File]
    for i,Number in enumerate(Numbers):
        for j,Digit in enumerate(Number):
            if Digit == "=":
                Numbers[i][j] = "-2"
            elif Digit == "-":
                Numbers[i][j] = "-1"
    Numbers = [[int(x) for x in Number] for Number in Numbers]
    return Numbers
    
def solveA(Numbers):
    DecimalSum = 0
    for Number in Numbers:
        Decimal = 0
        NumDigits = len(Number)
        for i in range(NumDigits):
            Decimal += Number[NumDigits-i-1] * 5**i
        DecimalSum += Decimal

    Output = ""
    while DecimalSum:
        rem = DecimalSum % 5
        DecimalSum //= 5
    
        if rem <= 2:
            Output = str(rem) + Output
        else:
            Output = "   =-"[rem] + Output
            DecimalSum += 1

    return Output

def solveB(Input):
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
