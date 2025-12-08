def ReadInputsA():
    File = open("./Inputs.txt", "r")
    results = [line.split() for line in File]
    results = [list(column) for column in zip(*results)]
    return results

def ReadInputsB():
    File = open("./Inputs.txt", "r")
    results = [list(line) for line in File]
    results = [list(column) for column in zip(*results)]
    problems = []
    temp = []

    for result in results:
        if any(r != " " for r in result ):
            temp.append(result)
        else:
            problems.append(temp)
            temp = []
    problems.append(temp)    
    return problems
                
    
def solveA(Input):
    answers = []
    for problem in Input:
        if problem[-1] == "*":
            res = 1
            for num in problem[:-1]:
                res *=int(num)
            answers.append(res)
        else:
            res = 0
            for num in problem[:-1]:
                res += int(num)
            answers.append(res)
    return sum(answers)

def solveB(Input):
    answers = []
    for problem in Input:
        if problem[0][-1] == "*":
            res = 1
            for num in problem:
                res *= int("".join(num[:-1]))
            answers.append(res)
        else:
            res = 0
            for num in problem:
                res += int("".join(num[:-1]))
            answers.append(res)

    return sum(answers)

def main():

    Input=ReadInputsA()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Input = ReadInputsB()
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
