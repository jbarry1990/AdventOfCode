import sympy

def ReadInputs():
        File = open("./Inputs.txt", "r")
        Data = File.read().strip()
        Solved = {}
        Equations = {}
        for Line in Data.split("\n"):
            Words = Line.split()
            if len(Words) == 2:
                Solved[Words[0][:-1]] = int(Words[1])
            else:
                Equations[Words[0][:-1]] = " ".join(Words[1:])

        return Solved, Equations


    
def solveA(Solved, Equations):
    DeleteKeys = []
    while len(Equations) > 0:
        
        for Key in DeleteKeys:
             Equations.pop(Key)
        DeleteKeys = []

        for Key, Value in Equations.items():
            if Value[:4] in Solved and Value[-4:] in Solved:
                Equations[Key] = str(Solved[Value[:4]]) + str(Value[4:-4]) + str(Solved[Value[-4:]])
                Solved[Key] = eval(Equations[Key])
                DeleteKeys.append(Key)

    
    return int(Solved["root"])

def solveB(Solved, Equations):
    Answer = 0
    monkeys = { "humn": sympy.Symbol("x") }

    x = [line.strip() for line in open(0)]

    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    for a in x:
        name, expr = a.split(": ")
        if name in monkeys: continue
        if expr.isdigit():
            monkeys[name] = sympy.Integer(expr)
        else:
            left, op, right = expr.split()
            if left in monkeys and right in monkeys:
                if name == "root":
                    Answer = sympy.solve(monkeys[left] - monkeys[right])[0]
                    break
                monkeys[name] = ops[op](monkeys[left], monkeys[right])
            else:
                x.append(a)
    return Answer

def main():

    Solved, Equations=ReadInputs()
    Part1=solveA(Solved, Equations)
    print("Answer: ", Part1)
    Solved, Equations=ReadInputs()
    Part2=solveB(Solved,Equations)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
