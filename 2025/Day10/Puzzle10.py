from collections import deque
import z3
def ReadInputs():
    File = open("./Inputs.txt", "r")
    Lines = File.readlines()
    machines = {i:{"lights" : [], "buttons":[], "power":[]} for i in range(len(Lines))}

    for i,line in enumerate(Lines):
        items = line.strip().split(" ")
        for item in items:
            if item.startswith("["):
                machines[i]["lights"] = list(item[1:-1])
            elif item.startswith("("):
                if "," in item:
                    machines[i]["buttons"].append([int(x) for x in item[1:-1].split(",")])
                else:
                    machines[i]["buttons"].append([int(item[1:-1])])
            elif item.startswith("{"):
                machines[i]["power"] = [int(x) for x in item[1:-1].split(",")]

    return machines

def solveA(Input):
    press_nums = []
    for machine in Input.items():
        goal = machine[1]["lights"]
        lights = ["." for _ in range(len(goal))]
        buttons = machine[1]["buttons"]
        queue = deque([])
        for b in buttons:
            queue.append((lights,buttons,[b]))
        seen = set()
        while len(queue) != 0:

            (l,b,attempts) = queue.popleft()
            l = l.copy()
            b= b.copy()
            attempts = attempts.copy()

            seen.add(("".join(l),b.index(attempts[-1])))

            for i in attempts[-1]:
                if l[i] == "#":
                    l[i] = "."
                else:
                    l[i] = "#"
               
            if l == goal:
                press_nums.append(len(attempts))
                break

            for i in b:
                temp = attempts.copy()
                if i != attempts[-1] and ("".join(l),b.index(i)) not in seen:
                    temp.append(i)
                    queue.append((l,b,temp))

                      
    return sum(press_nums)
                
def solveB(Input):
    num_presses = []
    for machine in Input.items():
        joltages = machine[1]["power"]
        buttons = machine[1]["buttons"]

        o = z3.Optimize()
        vars = z3.Ints(f"n{i}" for i in range(len(buttons)))
        for var in vars:
            o.add(var >= 0)
        for i,joltage in enumerate(joltages):
            equation = 0
            for j,button in enumerate(buttons):
                if i in button:
                    equation += vars[j]
            o.add(equation == joltage)
        o.minimize(sum(vars))
        o.check()
        num_presses.append(o.model().eval(sum(vars)).as_long())

    return sum(num_presses)


def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
