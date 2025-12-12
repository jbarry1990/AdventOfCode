from collections import deque
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
    return

def main():

    Input=ReadInputs()
    Part1=solveA(Input)
    print("Answer: ", Part1)
    Part2=solveB(Input)
    print("Answer: ", Part2)




   
if __name__ == "__main__":
    main()
