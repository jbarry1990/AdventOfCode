
def ReadFile(filename):
    with open(filename, "r") as f:
        content = f.readlines()

    return content

def check(total, equation,sign="+"):
    if total > equation[0]:
        return False
    elif total >= equation[0] and len(equation) > 1:
        return False
    elif total == equation[0] and len(equation) == 1:
        return True
    elif total < equation[0] and len(equation) == 1:
        return False
    else:
        if sign == "+":
            new_equation = equation.copy()
            new_total = total + new_equation.pop(1)
            if not check(new_total,new_equation,"+"):
                return check(total,equation,"*")
        else:
            new_equation = equation.copy()
            new_total = total * new_equation.pop(1)
            return check(new_total,new_equation,"+")

    return True
def PartASolve(inputs):
    equations = []
    for line in inputs:
        equation = []
        target,numbers = line.split(": ")
        equation.append(int(target))
        numbers = [int(x) for x in numbers.split(" ")]
        for num in numbers:
            equation.append(num)
        equations.append(equation)

    valid = []
    for equation in equations:
        Include = check(equation.pop(1), equation)
        if Include:
            valid.append(equation[0])
    return sum(valid)

def PartBSolve(inputs):
    return

def main():
    inputs = ReadFile("Inputs.txt")
    answer = PartASolve(inputs)
    print("Part A Answer: ", answer)
    answer = PartBSolve(inputs)
    print("Part B Answer: ", answer)

if __name__ == "__main__":
    main()
